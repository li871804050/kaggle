from pyspark import SparkContext
from pyspark.ml.feature import HashingTF,IDF,Tokenizer
from pyspark.sql import SparkSession
import os
os.environ['SPARK_HOME']='F:/hadoop/spark-2.3.2-bin-hadoop2.7'
os.environ['PYSPARK_PYTHON']='D:/ProgramData/Anaconda3/envs/tfColne/python.exe'

if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("Word Count").getOrCreate()
    sentenceData = spark.createDataFrame(
        [(0, "I heard about Spark and I love Spark"), (0, "I wish Java could use case classes"),
         (1, "Logistic regression models are neat")]).toDF("label", "sentence")
    #设置分词并调用
    tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
    wordsData = tokenizer.transform(sentenceData)

    #设置词转hash并调用
    hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
    featuriesData = hashingTF.transform(wordsData)

    #设置idf模型，并计算
    idf = IDF(inputCol="rawFeatures", outputCol="features")
    idfModel = idf.fit(featuriesData)
    rescalaData = idfModel.transform(featuriesData)

    #结果显示
    rescalaData.select("label", "features").show()