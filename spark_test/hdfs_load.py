import pyhdfs
import hdfs

if __name__ == '__main__':
    # client = pyhdfs.HdfsClient(hosts='127.0.0.1:50070', user_name='Administrator')
    # # client = client.get_active_namenode()
    # client.mkdirs('/hadoop')
    # print(client.listdir("/"))
    # client.copy_from_local('E:/data/test/pku98/199801.txt', '/dfs/1.txt')
    # print(client.listdir("/"))
    client = hdfs.Client(url='http://127.0.0.1:50070')
    client.makedirs('/test/hdfs', permission=777)
    client.upload('/test/hdfs', 'E:/data/test/pku98/199801.txt', overwrite=False)

