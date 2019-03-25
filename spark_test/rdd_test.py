from pyspark import SparkContext
import os
os.environ['SPARK_HOME']='F:/hadoop/spark-2.3.2-bin-hadoop2.7'
os.environ['PYSPARK_PYTHON']='D:/ProgramData/Anaconda3/envs/tfColne/python.exe'


if __name__ == '__main__':
    sc = SparkContext('local', 'test')
    test_data = sc.range(0, 100)
    td = test_data.map(lambda d: (d % 5, d))
    ts = td.reduceByKey(lambda a,b: a + b)
    dt = sc.range(10)
    dm = dt.map(lambda d: (d % 5, d))
    dg = dm.reduceByKey(lambda a, b: (a, b))
    ds = dg.sortByKey(ascending=False)
    print(ts.collect())
    print(ds.collect())
    print(ts.join(ds).collect())

    broad = sc.parallelize([1, 8, 2, 4])
    acc = sc.accumulator(0)
    broad.foreach(lambda x: acc.add(x))
    print(acc.value)