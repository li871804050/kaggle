import numpy as np

if __name__ == '__main__':
    data = [[ 0.9526, -0.246 , -0.8856],[ 0.5639, 0.2379, 0.9104]]
    #对象转化为 多维数组
    data = np.asarray(data)
    print(data)
    #简单的对应元素进行运算 非矩阵运算
    print(data * 10)
    print(data + 10)
    print(data + data)

    #获取矩阵的大小
    print(data.shape)

    #维度 zeros 生成全0矩阵
    print(np.zeros(shape=(3, 3, 1)).ndim)

    #numpy 内置range
    print(np.arange(15))

    #生成对角线上为1 其他地方为0 的单位方阵
    print(np.eye(10))

    #astype 类型转化
    print(np.arange(15).astype(np.float64))

    #相同大小的数组间的算术运算，其操作作用在对应的元素上
    arr = np.array([[1., 2., 3.], [4., 5., 6.]])
    print(arr ** 0.5)

    #数组拷贝 需使用copy()
    a = arr[1]
    b = arr[1][:]
    print(a, b)
    arr[1] = 0
    print(a, b)
    #使用 np.dot 计算内部矩阵来产生 XTX`
    a = np.arange(16).reshape((16, 1))
    print(a)
    print(np.dot(a, a.T))