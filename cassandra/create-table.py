from cassandra.cluster import Cluster
import config

cluster = Cluster(['35.163.17.140', '34.210.159.192','52.13.218.79','54.244.134.26'])
session = cluster.connect()

session.execute('DROP TABLE IF EXISTS blockchain;')
session.execute('CREATE TABLE data (txn_timestamp timestamp, from_wallet text, to_wallet text, amt int, PRIMARY KEY (txn_timestamp, from_wallet) );')
