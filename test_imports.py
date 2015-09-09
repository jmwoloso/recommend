#!/usr/bin/python
# Tests whether the pyspark modules can be imported at run time
import sys
import os


# path for spark source folder
os.environ['SPARK_HOME']="/home/jason/source/packages/non-python/spark"
# append pyspark to Python Path
sys.path.append("/home/jason/source/packages/non-python/spark/python")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print("Successfully imported Spark Modules")

except ImportError as e:
    print("Cannot import Spark Modules", e)
    sys.exit(1)
