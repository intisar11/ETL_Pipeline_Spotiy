from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext
import os


#set Java home
os.environ["Java Home"] = ("/Users/intisarahmed/Desktop/Java")

#Initiate Spark Context
conf = SparkConf().setAppName("Example").setMaster("Local").set('Spark.driver.extraClassPath', )

