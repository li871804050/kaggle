
global F

def get_find(A):
    l = len(A)
    F = [[1 for x in range(l + 1)]  for x in range(l)]
    for i in range(l, -1, -1):
        for j in range(l + 1, -1, -1):
            if i < j:
                F[i][j] = 1
            else:
                F[i][j] = A[j]%2


#i,j 相同时结果与后一位无关为arr[i]
#i > j 时 若后一位为0 则结果为1
#其他情况只与arr[i]的奇偶相关 pow(a, b) b 为大于0 的正整数时 奇偶至于a有关
def solve(arr, queries):
    res = []
    for query in queries:
        if query[0] == query[1]:
            if arr[query[0] - 1] % 2 == 0:
                res.append('Even')
            else:
                res.append('Odd')
        elif query[0] < len(arr) and arr[query[0]] == 0:
            res.append('Odd')
        elif arr[query[0] - 1] % 2 == 0:
            res.append('Even')
        else:
            res.append('Odd')
    return res
if __name__ == '__main__':
    arr = '3 2 7 3 3 2 3 8 6 1 6 0 7 1 9 1 5 0 1 4 9 6 8 2 4 6 5 3 4 7 4 7 1 4 0 4 8 3 3 4 6 1 5 5 4 6 6 9 6 7 5 6 4 3 0 5 2 5 3 8 5 0 1 6 6 7 3 4 0 4 0 3 1 5 3 5 1 1 4 0 3 1 8 5 7 8 5 1 6 0 4 1 2 4 9 0 1 4 4 3'
    arr = arr.split(' ')
    arr = [int(x) for x in arr]
    reader = open('data/input.txt', 'r')
    lines = reader.readlines()
    queries = []
    for line in lines:
        query = [int(x) for x in line.split(' ')]
        queries.append(query)
    reader.close()
    res = solve(arr, queries)
    writer = open('data/outpur.txt', 'w')
    for r in res:
        writer.write(r + '\r')
    writer.close()