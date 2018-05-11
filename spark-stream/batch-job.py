from pyspark.sql import SparkSession

spark2 = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
df = spark2.read.json("/home/ubuntu/s3files/txns-000000000000.json")

Witn NULL
df.select("timestamp",explode("inputs"), "outputs").select("timestamp","col.input_pubkey_base58", explode("outputs")).select("input_pubkey_base58", "col.output_pubkey_base58", "timestamp", "col.output_satoshis").show()

Before NULL
df.select("timestamp",explode("inputs"), "outputs").select("timestamp","col.input_pubkey_base58", explode("outputs")).filter("input_pubkey_base58 is not NULL").select("input_pubkey_base58", "col.output_pubkey_base58", "timestamp", "col.output_satoshis").filter("output_pubkey_base58 is not NULL").show()


import org.apache.spark.sql.{Row, SQLContext}
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.functions._
/**
* Created by vgiridatabricks on 5/16/16.
*/
object ExplodeDemo {
def main(args: Array[String]) : Unit = {
val conf = new SparkConf()
.setAppName(“csvParser”)
.setMaster(“local”)
val sc = new SparkContext(conf)
val sqlContext = new SQLContext(sc)
import sqlContext.implicits._
val df = sc.parallelize(Seq((1, Seq(2,3,4), Seq(5,6,7)), (2, Seq(3,4,5), Seq(6,7,8)), (3, Seq(4,5,6), Seq(7,8,9)))).toDF(“a”, “b”, “c”)
val df1 = df.select(df(“a”),explode(df(“b”)).alias(“b_columns”),df(“c”))
val df2 = df1.select(df1(“a”),df1(“b_columns”),explode(df1(“c”).alias(“c_columns”))).show()
}

}

>>> spark
<pyspark.sql.session.SparkSession object at 0x7f682f0cac10>
>>> spark._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", "<key>")
>>> spark._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", "AKIAIRD6NPSEANTK25PQ")
>>> spark.__jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey","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")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SparkSession' object has no attribute '__jsc'
>>> spark._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey","U5or4SCK/cZBOIh7CfhclWOrbU5+V8HIeBsSlxPc")
>>> data = sparkContext.textFile("s3n://"U5or4SCK/cZBOIh7CfhclWOrbU5+V8HIeBsSlxPc"@/bitcoin-blockchain-de18b/txns/txns-000000000000.json")
Traceback (most recent call last):
  File "/usr/local/spark/python/pyspark/context.py", line 237, in signal_handler
    raise KeyboardInterrupt()
KeyboardInterrupt
>>> data = sparkContext.textFile("s3n://bitcoin-blockchain-de18b/txns/txns-000000000000.json")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sparkContext' is not defined
>>> data = spark.textFile("s3n://bitcoin-blockchain-de18b/txns/txns-000000000000.json")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SparkSession' object has no attribute 'textFile'
>>> spark
<pyspark.sql.session.SparkSession object at 0x7f682f0cac10>
>>> sc
<SparkContext master=local[*] appName=PySparkShell>
>>> data = sc.textFile("s3n://bitcoin-blockchain-de18b/txns/txns-000000000000.json")
>>> data
s3n://bitcoin-blockchain-de18b/txns/txns-000000000000.json MapPartitionsRDD[1] at textFile at NativeMethodAccessorImpl.java:0
>>> data.show()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'RDD' object has no attribute 'show'
>>> data = sc.textFile("s3n://bitcoin-blockchain-de18b/txns/txns-000000000000.json")
