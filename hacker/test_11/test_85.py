import numpy as np
class Solution:
    def maximalRectangle(self, matrix: [[str]]) -> int:
        if len(matrix) == 0:
            return 0
        area = 0
        res = np.zeros(shape=(len(matrix), len(matrix[0]), 2))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0' :
                    res[i][j] = [0, 0]
                else:
                    if i == 0:
                        res[i][j][0] = 1
                    else:
                        res[i][j][0] = res[i - 1][j][0] + 1
                    if j == 0:
                        res[i][j][1] = 1
                    else:
                        res[i][j][1] = res[i][j - 1][1] + 1
                area = max(area, res[i][j][0], res[i][j][1])
                if i > 0 and matrix[i - 1][j] == '1':
                    for k in range(1, int(res[i][j][0])):
                        area = max(res[i - k:i + 1,j, 1].min() * (k + 1), area)

        return area

if __name__ == '__main__':
    solution = Solution()
    matrix =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(solution.maximalRectangle(matrix))

