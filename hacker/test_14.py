import copy
ALL_POINT = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_input_all(board, i ,j):
    nums = copy.deepcopy(ALL_POINT)
    for k in range(9):
        if board[i][k] in nums:
            nums.remove(board[i][k])
        if board[k][j] in nums:
            nums.remove(board[k][j])
    m = (int(i / 3)) * 3
    n = (int(j / 3)) * 3
    for x in range(3):
        for y in range(3):
            if board[x + m][y + n] in nums:
                nums.remove(board[x + m][y + n])
    return nums

def get_input_only(board, i ,j):
    nums = copy.deepcopy(board[i][j])
    for k in range(9):
        if k != j and len(board[i][k]) > 1:
            for b in board[i][k]:
                if b in nums:
                    nums.remove(b)
    if len(nums) == 1:
        return nums[0]
    nums = copy.deepcopy(board[i][j])
    for k in range(9):
        if k != i and len(board[k][j]) > 1:
            for b in board[k][j]:
                if b in nums:
                    nums.remove(b)
    if len(nums) == 1:
        return nums[0]
    m = (int(i / 3)) * 3
    n = (int(j / 3)) * 3
    nums = copy.deepcopy(board[i][j])
    for x in range(3):
        for y in range(3):
            if x + m == i and y + n == j:
                continue
            if len(board[x + m][y + n]) > 1:
                for b in nums:
                    nums.remove(b)
    if len(nums) == 1:
        return nums[0]
    return None


def input_blank(board):
    old_blank = 0
    while True:
        find_blank = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.' or len(board[i][j]) > 1:
                    find_blank += 1
                    all = get_input_all(board, i, j)
                    if len(all) == 0:
                        return 1
                    elif len(all) == 1:
                        board[i][j] = all[0]
                    else:
                        board[i][j] = all
        if find_blank == 0:
            return 2
        if find_blank == old_blank:
            return 3
        old_blank = find_blank

def try_input(board, pos_list, try_map, board_map):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.' or len(board[i][j]) > 1:
                all = get_input_all(board, i, j)
                pos_list.append(str(i) + str(j))
                for a in all:
                    if str(i) + str(j) not in try_map.keys():
                        n_board = copy.deepcopy(board)
                        board_map[str(i) + str(j)] = n_board
                        try_map[str(i) + str(j)] = [a]
                        board[i][j] = a
                        return
                    else:
                        if a not in try_map[str(i) + str(j)]:
                            try_map[str(i) + str(j)].append(a)
                            board[i][j] = a
                            return

def input_error(pos_list,try_map, board_map):
    while True:
        pos = pos_list.pop()
        i = int(pos[0])
        j = int(pos[1])
        board = copy.deepcopy(board_map[pos])
        all = get_input_all(board, i, j)
        if all != try_map[pos]:
            pos_list.append(str(i) + str(j))
            for a in all:
                if a not in try_map[str(i) + str(j)]:
                    try_map[str(i) + str(j)].append(a)
                    board[i][j] = a
                    return board
        else:
            try_map.pop(pos)
            board_map.pop(pos)

def solveSudoku(board: [[]]):
    board_map = {}
    try_map = {}
    pos_list = []
    while True:
        err = input_blank(board)
        if err == 2:
            return board
        if err == 1:
            board = input_error(pos_list, try_map, board_map)
        elif err == 3:
            try_input(board, pos_list, try_map, board_map)




if __name__ == '__main__':
    l = [[".","6","5",".","7",".","9",".","."],
         [".",".",".",".",".","4","5",".","3"],
         [".","7",".",".",".",".",".",".","."],
         ["7","2",".",".","1",".",".","9","."],
         [".",".","4",".",".",".","8",".","."],
         [".","9",".",".","8",".",".","1","2"],
         [".",".",".",".",".",".",".","2","."],
         ["2",".","7","8",".",".",".",".","."],
         [".",".","3",".","5",".","7","6","."]]
    print(solveSudoku(l))
    # print(l)