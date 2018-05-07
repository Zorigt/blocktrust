from cassandra.cluster import Cluster
import config

cluster = Cluster(['35.163.17.140', '34.210.159.192','52.13.218.79','54.244.134.26'])
session = cluster.connect()

session.execute('DROP TABLE IF EXISTS txns3;')
session.execute('CREATE TABLE txns3 (txn_date timestamp, from_wallet text, to_wallet text, amt bigint, PRIMARY KEY (txn_date, from_wallet, to_wallet) ) WITH CLUSTERING ORDER BY (temp ASC, to_wallet DESC,txn_date DESC);')
