from surprise import SVD
from surprise import Dataset
from surprise import accuracy,Reader
from surprise.model_selection import train_test_split
import os
# 指定文件路径数据格式必须为 user item rating [timestamp]
file_path = os.path.expanduser('E:/git/kaggle/offline/data/user.csv')
# 指定文件格式
reader = Reader(line_format='user item rating timestamp', sep=',')
# 从文件读取数据
music_data = Dataset.load_from_file(file_path, reader=reader)
# 分成5折
music_data.split(n_folds=5)

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset, testset = train_test_split(music_data, test_size=.25)

# We'll use the famous SVD algorithm.
algo = SVD()

# Train the algorithm on the trainset, and predict ratings for the testset
algo.fit(trainset)
predictions = algo.test(testset)

# Then compute RMSE
accuracy.rmse(predictions)

