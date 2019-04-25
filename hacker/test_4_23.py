def uniquePathsWithObstacles(obstacleGrid: [[int]]) -> int:
    down_path = []
    i = 0
    j = 0
    l_d = len(obstacleGrid) - 1
    l_r = len(obstacleGrid[0]) - 1
    count = 0
    while True:
        if j + 1 <= l_r and obstacleGrid[i][j + 1] == 0:
            if i + 1 <= l_d and obstacleGrid[i + 1][j] == 0:
                down_path.append([i + 1, j])
            j = j + 1
        elif i + 1 <= l_d and obstacleGrid[i + 1][j] == 0 :
            i = i + 1
        else:
            if i == l_d and j == l_r and obstacleGrid[i][j] == 0:
                count += 1
            if len(down_path) > 0:
                [i, j] = down_path.pop()
            else:
                break
    return count

def uniquePathsWithObstacles2(obstacleGrid: [[int]]) -> int:
    path = [[0 for i in obstacleGrid[0]] for j in obstacleGrid]
    j = len(obstacleGrid[0]) - 1
    i = len(obstacleGrid) - 1
    if obstacleGrid[i][j] == 1:
        return 0
    path[i][j] = 1
    for x in range(i - 1, -1, -1):
        if obstacleGrid[x][j] == 0 :
            path[x][j] = path[x + 1][j]
    for y in range(j - 1, -1, -1):
        if obstacleGrid[i][y] == 0 :
            path[i][y] = path[i][y + 1]

    for x in range(i - 1, -1, -1):
        for y in range(j - 1, -1, -1):
            if obstacleGrid[x][y] == 0:
                path[x][y] = path[x + 1][y] + path[x][y + 1]
    return path[0][0]

def minPathSum(grid: [[int]]) -> int:
    res = [[0 for i in grid[0]] for j in grid]
    x = len(grid) - 1
    y = len(grid[0]) - 1
    res[x][y] = grid[x][y]
    for i in range(x - 1, -1, -1):
        res[i][y] = grid[i][y] + res[i + 1][y]
    for j in range(y - 1, -1, -1):
        res[x][j] = grid[x][j] + res[x][j + 1]
    for i in range(x - 1, -1, -1):
        for j in range(y - 1, -1, -1):
            res[i][j] = min(res[i + 1][j], res[i][j + 1]) + grid[i][j]
    return res[0][0]


if __name__ == '__main__':
    path = [[0,0,0],[0,1,0],[0,0,0]]
    print(uniquePathsWithObstacles2(path))