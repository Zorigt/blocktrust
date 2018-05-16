import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
# cassandra
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from cassandra import ConsistencyLevel


#testing
from pyspark.sql import DataFrame
from pyspark.rdd import RDD
import collections
import time
import datetime

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def printJson(iter):
    print("print parsed json")
    for i in iter:
    	print(convert(i))

def sendCassandra(iter):
    print("send to cassandra")
    cluster = Cluster(['52.36.211.47', '52.38.24.8','52.34.60.38'])
    session = cluster.connect()
    session.set_keyspace("blocktrust")

    insert_statement = session.prepare("INSERT INTO txns (from_wallet, to_wallet, txn_date, amt) VALUES (?, ?, ?, ?)")

    count = 0
    # batch insert into cassandra database
    batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)

    for record in iter:
        record2 = convert(record)
        inputs = record2['inputs']
        outputs = record2['outputs']
        for input in inputs:
            if input.get('input_pubkey_base58'):
                #print(input['input_pubkey_base58'])
                for output in outputs:
                    #print(output['output_pubkey_base58'])
                    if output.get('output_pubkey_base58'):
                        #print(output['output_pubkey_base58'])
                        batch.add(insert_statement, (input['input_pubkey_base58'], output['output_pubkey_base58'], int(record2['timestamp']), int(output['output_satoshis'])))

                        # split the batch, so that the batch will not exceed the size limit
                        count += 1
                        if count % 500 == 0:
                            print(count)
                            session.execute(batch)
                            batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)

    # send the batch that is less than 500
    session.execute(batch)
    session.shutdown()

def f(rdd):
	rows = rdd.collect()
     	for r in rows:
        	print r

if __name__ == "__main__":
    sc = SparkContext(appName="PySparkShell")
    ssc = StreamingContext(sc, 2) # 2 second window
    broker, topic = sys.argv[1:]
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": broker})
    # Parse the inbound message as json
    parsed = kvs.map(lambda v: json.loads(v[1]))
    #lines = kvs.map(lambda x: x[1])
    parsed.foreachRDD(lambda rdd: rdd.foreachPartition(sendCassandra))
    ssc.start()
    ssc.awaitTermination()