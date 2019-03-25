from pandas import Series

if __name__ == '__main__':
    #Series是一个定长的，有序的字典
    obj = Series([4, 7, -5, 3])
    print(obj)
    print(obj.values)

    obj2 = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
    print(obj2)

    #只传递一个字典的时候，结果Series中的索引将是排序后的字典的建
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3 = Series(sdata)
    print(obj3)

    #控制顺序 不存在的 NAN填充
    states = ['Utah', 'Ohio', 'Oregon', 'Texas']
    obj4 = Series(sdata, index=states)
    print(obj4)

    print(obj4 + obj3)

    #Series的索引可以通过赋值就地更改
    obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
    print(obj)