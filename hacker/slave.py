import numpy as np
from math import factorial
INT = 1000000007

res = [[0 for y in range(1000 + 1)] for x in range(2000 + 1) ]
for i in range(2001):
    for j in range(1001):
        if j > i:
            break
        if j <= 0 or i == j:
            res[i][j] = 1
        else:
            res[i][j] = (res[i - 1][j] + res[i - 1][j - 1])
            if (i + j) % 10 == 0:
                res[i][j] = res[i][j] % INT
def solve(n, m):
    if m == 1:
        return 1
    m = m - 1
    return int(res[m+n][n]%INT)


def change_to(m, n):
    if m <= 1 or n <= 1:
        return 1
    else:
        return change_to(m - 1, n) + change_to(m - 1, n - 1)

if __name__ == '__main__':
    # for i in range(2, 10):
    #     for j in range(2, 10):
    #         print(solve(j, i))
    print(solve(522, 575))
    # print("455304470")