import datetime

def arrayManipulation(n, queries):
    data = [0 for x in range(n + 1)]
    max = 0
    for i in range(len(queries)):
        data[queries[i][0]] += queries[i][2]
        if queries[i][1] + 1 <= n:
            data[queries[i][1] + 1] -= queries[i][2]
    x = 0
    for i in data:
        x += i
        if max < x:
            max = x
    return max

def slove_1(n, queries):
    data = [0 for x in range(n + 1)]
    max = 0
    for i in range(len(queries)):
        data[queries[i][0]] += queries[i][2]
        data[queries[i][1] + 1] -= queries[i][2]
    for i in data:
        if max < max + i:
            max = max + i
    return max

def slove_2(n, queries):
    data = [0 for x in range(n)]
    max = 0
    for i in range(n):
        for j in range(len(queries)):
            if queries[j][0] - 1 <= i and queries[j][1] - 1 >=i:
                data[i] += queries[j][2]
        if max < data[i]:
            max = data[i]
    return max

if __name__ == '__main__':
    # n = 10
    # queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1],[5, 9, 15]]
    # n = 5
    # queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    n = 10000000
    reader = open('data/input_3.txt', 'r')
    queries = []
    for line in reader.readlines():
        query = [int(x) for x in line.split(' ')]
        queries.append(query)
    print(slove_1(n, queries))
    # result = 0
    # for i in data:
    #     if i > result:
    #         result = i
    # print(result)
    print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    print(int(2484930878))