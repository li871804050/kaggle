def numIslands(grid:[[]]) -> int:
    land = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                land += 1
                land_pos = []
                land_pos.append([i, j])
                pos = 0
                while True:
                    find = 0
                    [x, y] = land_pos[pos]
                    pos += 1
                    for k in range(y + 1, len(grid[0])):
                        if grid[x][k] != "0":
                            grid[x][k] = "0"
                            if [x, k] not in land_pos:
                                land_pos.append([x, k])
                                find = 1
                        else:
                            break
                    for k in range(x + 1, len(grid)):
                        if grid[k][y] != "0":
                            grid[k][y] = "0"
                            if [k, y] not in land_pos:
                                land_pos.append([k, y])
                                find = 1
                        else:
                            break

                    for k in range(y - 1, -1, -1):
                        if grid[x][k] != "0":
                            grid[x][k] = "0"
                            if [x, k] not in land_pos:
                                land_pos.append([x, k])
                                find = 1
                        else:
                            break
                    for k in range(x - 1, -1, -1):
                        if grid[k][y] != "0":
                            grid[k][y] = "0"
                            if [k, y] not in land_pos:
                                land_pos.append([k, y])
                                find = 1
                        else:
                            break

                    if find == 0 and pos == len(land_pos):
                        break
    return land

if __name__ == '__main__':
    s = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(numIslands(s))
    print([x for x in range(4, 0, -1)])