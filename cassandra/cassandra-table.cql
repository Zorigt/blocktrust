cqlsh> CREATE KEYSPACE bt WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};
cqlsh> use bt
   ... ;
cqlsh:bt> CREATE TABLE txns (id text, date text, time timestamp, PRIMARY KEY ((id, date), time), ) WITH CLUSTERING ORDER BY (time DESC); 


CREATE TABLE txns (id text PRIMARY KEY);

spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 spark-kafka.py localhost:9092 price_data_part4 

https://github.com/apache/spark/blob/master/examples/src/main/python/streaming/direct_kafka_wordcount.py

python -m py_compile script.py

kafka-console-producer.sh --broker-list localhost:9092 --topic my_topic
--new-producer < my_file.txt