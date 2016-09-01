import os
import sys

# spark home
spark_home = os.environ.get('SPARK_HOME', None)
spark_version = os.environ.get('SPARK_VERSION', '2.0.0')
if not spark_home:
    raise ValueError('SPARK_HOME environment variable is not set')


# If Spark V1.4.x is detected, then add ' pyspark-shell' to
# # the end of the 'PYSPARK_SUBMIT_ARGS' environment variable
spark_release_file = spark_home + "/RELEASE"
if os.path.exists(spark_release_file) and "Spark " + spark_version in open(spark_release_file).read():
    # default_submit = "--master local[*] --executor-memory 32G --driver-memory 32G"
    default_submit = "--master local[*] --executor-memory 8G --driver-memory 8G"
    pyspark_submit_args = os.environ.get("PYSPARK_SUBMIT_ARGS", default_submit)
    if "pyspark-shell" not in pyspark_submit_args:
        pyspark_submit_args += " pyspark-shell"
        os.environ["PYSPARK_SUBMIT_ARGS"] = pyspark_submit_args

# Add the spark python sub-directory to the path
sys.path.insert(0, os.path.join(spark_home, 'python'))

# Add the py4j to the path
# You may need to change the version number to match your install
# sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.9-src.zip'))
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.10.1-src.zip'))

# Initialize PySpark to predefine the SparkContext variable 'sc'
execfile(os.path.join(spark_home, 'python/pyspark/shell.py'))
