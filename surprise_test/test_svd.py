from surprise import SVD
from surprise import Dataset
from surprise import accuracy,Reader
from surprise.model_selection import train_test_split
import os

# Load the movielens-100k dataset (download it if needed),
# data = Dataset.load_builtin('ml-100k')

# 指定文件所在路径
file_path = os.path.expanduser('E:/git/kaggle/surprise_test/ml-100k/u.data')
# 告诉文本阅读器，文本的格式是怎么样的
reader = Reader(line_format='user item rating timestamp', sep='\t')
# 加载数据
data = Dataset.load_from_file(file_path, reader=reader)
# 手动切分成5折(方便交叉验证)
data.split(n_folds=5)

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset, testset = train_test_split(data, test_size=.25)

# We'll use the famous SVD algorithm.
algo = SVD()

# Train the algorithm on the trainset, and predict ratings for the testset
algo.fit(trainset)
predictions = algo.test(testset)

# Then compute RMSE
accuracy.rmse(predictions)

