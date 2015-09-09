#!/usr/bin/python
# Tests whether the pyspark modules can be imported at run time
import sys
import os
import py4j

if 'SPARK_HOME' not in os.environ:
    # path for spark source folder
    os.environ['SPARK_HOME']="/home/jason/source/packages/non-python/spark"

SPARK_HOME = os.environ['SPARK_HOME']
# append pyspark/py4j to Python Path
sys.path.insert(0, os.path.join(SPARK_HOME, "python", "build"))
sys.path.insert(0, os.path.join(SPARK_HOME, "python"))


try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print("Successfully imported Spark Modules")

except ImportError as e:
    print("Cannot import Spark Modules", e)
    sys.exit(1)
