def get_cover(queries, data):
    print(data)
    if len(queries) > 0:
        start = 0
        end = 0
        queries_s = sorted(queries, key=lambda x: (x[0], x[2]))
        queries_e = sorted(queries, key=lambda x: (x[1], x[2]), reverse=True)
        queries_s_min = queries_s[len(queries_s) - 1][1]
        queries_e_max = queries_e[len(queries_e) - 1][0]
        for i in range(len(queries_e)):
            if queries_e[i][1] == queries_s_min:
                start = i
                break
        for j in range(len(queries_s)):
            if queries_s[j][0] == queries_e_max:
                end = j
                break
        if queries_s[end] not in data:
            data.append(queries_s[end][0: 2])
            get_cover(queries_s[end + 1:], data)
        if queries_e[start] not in data:
            data.append(queries_e[start][0: 2])
            get_cover(queries_e[start + 1:], data)

if __name__ == '__main__':
    # queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
    # data = []
    # get_cover(queries, data)
    # print(data)

    n = 10000000
    reader = open('data/input_3.txt', 'r')
    queries = []
    data = []
    # data = [0 for x in range(n)]
    for line in reader.readlines():
        query = [int(x) for x in line.split(' ')]
        queries.append(query)
    get_cover(queries, data)