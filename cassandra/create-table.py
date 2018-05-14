from cassandra.cluster import Cluster
import config

cluster = Cluster(config.CASSANDRA_SERVER)
# cluster = Cluster(['35.163.17.140', '34.210.159.192','52.13.218.79','54.244.134.26'])
session = cluster.connect(config.CASSANDRA_NAMESPACE)

session.execute('DROP TABLE IF EXISTS txns;')
session.execute('CREATE TABLE txns (from_wallet text, to_wallet text, txn_date bigint, amt bigint, PRIMARY KEY (from_wallet, to_wallet, txn_date) ) WITH CLUSTERING ORDER BY (to_wallet ASC,txn_date ASC);')
