from operator import add
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import os
os.environ['SPARK_HOME']='F:/hadoop/spark-2.3.2-bin-hadoop2.7'
os.environ['PYSPARK_PYTHON']='D:/ProgramData/Anaconda3/envs/tfColne/python.exe'


if __name__ == '__main__':
    sc = SparkContext('local', 'test')
    ssc = StreamingContext(sc, 20)
    #不能读取文件 应为文件夹
    lines = ssc.textFileStream('file:///E:/data/test/pku98/')
    words = lines.flatMap(lambda line: line.split(' '))
    wordCounts = words.map(lambda x: (x, 1)).reduceByKey(add)
    wordCounts.pprint()
    # 监听文件夹
    ssc.start()
    ssc.awaitTermination()