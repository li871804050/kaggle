from pyspark import SparkContext
import os
os.environ['SPARK_HOME']='F:/hadoop/spark-2.3.2-bin-hadoop2.7'
os.environ['PYSPARK_PYTHON']='D:/ProgramData/Anaconda3/envs/tfColne/python.exe'

if __name__ == '__main__':
    sc = SparkContext('local', 'test')
    textFile_loc = sc.textFile('file:///E:/data/test/pku98/199801.txt')
    textFile_hdfs = sc.textFile('hdfs://localhost:9000/test/bg/199801.txt')
    wordCount_loc = textFile_loc.flatMap(lambda line: line.split(' ')).map(lambda  word:(word, 1)).reduceByKey(
        lambda a, b: a + b)
    wordCount_hdfs = textFile_hdfs.flatMap(lambda line: line.split(' ')).map(lambda word: (word, 1)).reduceByKey(
        lambda a, b: a + b)
    print(wordCount_loc.collect())
    print(wordCount_hdfs.collect())