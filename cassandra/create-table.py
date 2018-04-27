from cassandra.cluster import Cluster
import config

cluster = Cluster(['35.163.17.140', '34.210.159.192','52.13.218.79','54.244.134.26'])
session = cluster.connect()

session.execute('DROP TABLE IF EXISTS blockchain;')
session.execute('CREATE TABLE data (userid int, time timestamp, status text, PRIMARY KEY (userid, time) ) WITH CLUSTERING ORDER BY (time DESC);')
