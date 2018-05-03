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

/usr/local/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic blocks < s3files/blocks-000000000000.json

/usr/local/kafka/bin/kafka-simple-consumer-shell.sh --broker-list localhost:9092 --topic txns --partition 0

/usr/local/kafka/bin/kafka-simple-consumer-shell.sh --broker-list localhost:9092 --topic txns --partition 1

spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 spark-kafka.py localhost:9092 txns

spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 spark-kafka.py localhost:9092 blocks

DROP TABLE IF EXISTS bt2.txns

CREATE TABLE IF NOT EXISTS bt2.txns;

http://ec2-35-163-17-140.us-west-2.compute.amazonaws.com:50070/dfshealth.html#tab-datanode

http://ec2-52-13-218-79.us-west-2.compute.amazonaws.com:8081/

cp /usr/local/kafka/config/server.properties /usr/local/kafka/config/server.properties.bk
vim /usr/local/kafka/config/server.properties 
replica.fetch.max.bytes=15728640
message.max.bytes=15728640

cp /usr/local/kafka/config/consumer.properties /usr/local/kafka/config/consumer.properties.bk
vim /usr/local/kafka/config/consumer.properties
fetch.message.max.bytes=15728640



curl --user zorigt --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "decoderawtransaction", "params": ["22660acb63be4dc2272adae2237476e0aa5dbe3b9b99e0fdeed9c7f6461dd877"] }' -H 'content-type: text/plain;' http://ec2-52-40-245-202.us-west-2.compute.amazonaws.com:8333

curl --user zorigt --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaccount", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX"] }' -H 'content-type: text/plain;' http://ec2-52-40-245-202.us-west-2.compute.amazonaws.com:8333

curl --user zorigt --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getpeerinfo", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX"] }' -H 'content-type: text/plain;' http://ec2-52-40-245-202.us-west-2.compute.amazonaws.com:8333

curl --user zorigt:pass --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getinfo","params":[]}' -H 'content-type:text/plain;' http://zorigt:pass@ec2-52-40-245-202.us-west-2.compute.amazonaws.com:8332/

curl --user zorigt:pass --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getmininginfo","params":[]}' -H 'content-type:text/plain;' http://52.40.245.202:8332/


[blockchain@blockchain ~]$ cat .bitcoin/bitcoin.conf 
debug=0
rpcuser=bitcoinrpc
rpcpassword=****************
server=1
daemon=1
bind=192.168.0.12
port=8332
#whitebind=192.168.0.12:8332
#whitelist=255.255.255.0
rpcallowip=192.168.0.0/24
rpcallowip=127.0.0.1

[blockchain@blockchain ~]$ curl --user bitcoinrpc --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/
{"result":{"version":110000,"protocolversion":70002,"walletversion":60000,"balance":0.00000000,"blocks":254929,"timeoffset":-1,"connections":8,"proxy":"","difficulty":65750060.14908481,"testnet":false,"keypoololdest":1441852887,"keypoolsize":101,"paytxfee":0.00000000,"relayfee":0.00001000,"errors":""},"error":null,"id":"curltest"}
[blockchain@blockchain ~]$ 
[blockchain@blockchain ~]$ 
[blockchain@blockchain ~]$ 
[blockchain@blockchain ~]$ curl --user bitcoinrpc --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://192.168.0.12:8332/
curl: (52) Empty reply from server


Spark Cluster WebUI is running at http://ec2-35-163-17-140.us-west-2.compute.amazonaws.com:8080
Spark Job WebUI is running at http://ec2-35-163-17-140.us-west-2.compute.amazonaws.com:4040
Spark Jupyter Notebook is running at http://ec2-35-163-17-140.us-west-2.compute.amazonaws.com:8888


from pyspark import SparkContext
parsed = spark.read.option("multiline", "true").json("/home/ubuntu/s3files/blocks-000000000000.json")
test = parsed.select("transactions.inputs").take(2)
test[0].inputs[2]
