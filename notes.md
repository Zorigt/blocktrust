cqlsh> CREATE KEYSPACE bt WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};
cqlsh> use bt
   ... ;
cqlsh:bt> CREATE TABLE txns (id text, date text, time timestamp, PRIMARY KEY ((id, date), time), ) WITH CLUSTERING ORDER BY (time DESC); 


CREATE TABLE txns (id text, date text, PRIMARY KEY);

spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 spark-kafka.py localhost:9092 price_data_part4 

https://github.com/apache/spark/blob/master/examples/src/main/python/streaming/direct_kafka_wordcount.py

python -m py_compile script.py

/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 2 --topic txns

/usr/local/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic txns < results-20180427-101409.csv 

/usr/local/kafka/bin/kafka-simple-consumer-shell.sh --broker-list localhost:9092 --topic txns --partition 0

/usr/local/kafka/bin/kafka-simple-consumer-shell.sh --broker-list localhost:9092 --topic txns --partition 1

spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 spark-kafka.py localhost:9092 txns

DROP TABLE IF EXISTS bt2.txns

CREATE TABLE IF NOT EXISTS bt2.txns;

http://ec2-35-163-17-140.us-west-2.compute.amazonaws.com:50070/dfshealth.html#tab-datanode

http://ec2-52-13-218-79.us-west-2.compute.amazonaws.com:8081/
