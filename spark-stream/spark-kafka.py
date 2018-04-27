import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
# cassandra
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from cassandra import ConsistencyLevel

def sendCassandra(iter):
    print("send to cassandra")
    cluster = Cluster(['35.163.17.140', '34.210.159.192','52.13.218.79','54.244.134.26'])
    session = cluster.connect()
    session.set_keyspace("bt2")

    insert_statement = session.prepare("INSERT INTO bt2.txns (id) VALUES (?)")

    count = 0

    # batch insert into cassandra database
    batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
    
    for record in iter:
        batch.add(insert_statement, (record[0]))


        # split the batch, so that the batch will not exceed the size limit
        count += 1
        if count % 500 == 0:
            session.execute(batch)
            batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)

    # send the batch that is less than 500            
    session.execute(batch)
    session.shutdown()

if __name__ == "__main__":
    sc = SparkContext(appName="blocktrust")
    ssc = StreamingContext(sc, 2) # 2 second window
    broker, topic = sys.argv[1:]
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": broker})

    lines = kvs.map(lambda x: x[1])
    lines.foreachRDD(lambda rdd: rdd.foreachPartition(sendCassandra))
    lines.pprint()
    ssc.start()
    ssc.awaitTermination()