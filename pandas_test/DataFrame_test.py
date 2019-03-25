from pandas import DataFrame,Series

#一个Datarame表示一个表格，类似电子表格的数据结构
# 包含一个经过排序的列表集，它们每一个都可以有不同的类型值

if __name__ == '__main__':
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    print(frame['year'].astype(str) +  frame['pop'].astype(str) + frame['state'])


    # #设置列的顺序
    # frame = DataFrame(data, columns=['year', 'state', 'pop'])
    # print(frame)
    #
    # #传递了一个行，但不包括在 data 中，在结果中它会表示为NA值
    # frame = DataFrame(data, columns=['year', 'state', 'pop', 'debt'])
    # print(frame)
    #
    # frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five'])
    # print( frame2.columns)
    # print(frame2['year'])       #列访问
    # print(frame2.ix['three'])   #索访问 行访问
    #
    # #通过列表或数组给一列赋值时，所赋的值的长度必须和DataFrame的长度相匹配。
    # # 如果你使用Series来赋值，它会代替在DataFrame中精确匹配的索引的值，并在说有的空洞插入丢失数据
    # #给一个不存在的列赋值，将会创建一个新的列
    # val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
    # # frame2['debt'] = val
    # frame2['debt'] = range(5)
    # print(frame2)
    #
    # #它的外部键会被解释为列索引，内部键会被解释为行索引
    # pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
    # frame3 = DataFrame(pop)
    # print(frame3)
    #
    # #索引对象是不可变的，因此不能由用户改变
    # obj = Series(range(3), index=['a', 'b', 'c'])
    # index = obj.index
    # print(obj)
    # # index[0] = '1'
    # #重新索引
    # obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    # print(obj2)