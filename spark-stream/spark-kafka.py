import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


if __name__ == "__main__":
    sc = SparkContext(appName="blocktrust")
    ssc = StreamingContext(sc, 2) # 2 second window
    broker, topic = sys.argv[1:]
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": broker})

    lines = kvs.map(lambda x: x[1])

    lines.pprint()
    ssc.start()
    ssc.awaitTermination()