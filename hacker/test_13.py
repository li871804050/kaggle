def solveSudoku(board: [[]]) -> None:
    find_blank_old = 0
    while True:
        while True:
            find_blank = 0
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.' or board[i][j] == [] or len(board[i][j]) > 1 or board[i][j] == '':
                        board[i][j] = '.'
                        find_blank += 1
                        in_p = input_point(i, j, board)
                        if in_p != None:
                            if len(in_p) == 1:
                                print(i + 1, j  + 1, in_p[0])
                                board[i][j] = in_p[0]
            if find_blank == 0 or find_blank_old == find_blank:
                break
            find_blank_old = find_blank
        if find_blank_old == 0:
            break

        find = get_in(board)
        if find == 0:
            break
        ol_find = 0
        while True:
            for i in range(9):
                for j in range(9):
                    if len(board[i][j]) > 1:
                        in_p2 = input_point2(i, j, board)
                        if in_p2 != None:
                            if len(in_p2) == 1:
                                print(i + 1, j + 1, in_p2[0])
                                board[i][j] = in_p2[0]
                                find = get_in(board)
                                break
            if find == 0 or find == ol_find:
                break
            else:
                ol_find = find

def get_in(board):
    find = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.' or board[i][j] == [] or len(board[i][j]) > 1:
                board[i][j] == '.'
                find = 1
                in_p = input_point(i, j, board)
                if in_p != None:
                    if len(in_p) == 1:
                        board[i][j] = in_p[0]
                    elif len(in_p) > 1:
                        board[i][j] = in_p
    return find


def input_point2(i: int, j: int, board: [[]]) -> None:
    input_2_1 = board[i][j][:]
    for x in range(9):
        if x == j:
            continue
        if len((board[i][x])) > 1:
            for b in board[i][x]:
                if b in input_2_1:
                    input_2_1.remove(b)
    if len(input_2_1) == 1:
        return input_2_1

    input_2_2 = board[i][j][:]
    for y in range(9):
        if y == i:
            continue
        if len(board[y][j]) > 1:
            for b in board[y][j]:
                if b in input_2_2:
                    input_2_2.remove(b)
    if len(input_2_2) == 1:
        return input_2_2

    input_2_3 = board[i][j][:]
    m = (int(i / 3)) * 3
    n = (int(j / 3)) * 3
    for x in range(3):
        for y in range(3):
            if x + m == i and y + n == j:
                continue
            if len(board[x + m][y + n]) > 1:
                for b in board[x + m][y + n]:
                    if b in input_2_3:
                        input_2_3.remove(b)
    if len(input_2_3) == 1:
        return input_2_3
    return None

def input_point(i:int, j:int, board:[[]]) ->str:
    # if i == 4 and j == 8:
    #     print(i , j)
    all_point = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in range(len(board)):
        if board[x][j] in all_point:
            all_point.remove(board[x][j])

    for y in range(len(board[0])):
        if board[i][y] in all_point:
            all_point.remove(board[i][y])
    m = (int(i / 3)) * 3
    n = (int(j / 3)) * 3
    for x in range(3):
        for y in range(3):
            if board[x + m][y + n] in all_point:
                all_point.remove(board[x + m][y + n])
    return all_point


def solveSudoku2(board: [[]]) -> None:
    while True:
        find_blank = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    find_blank = 1
                    in_p = input_point(i, j, board)
                    if in_p != None:
                        board[i][j] = in_p
        if find_blank == 0:
            break

if __name__ == '__main__':
    l = [[".","6","5",".","7",".","9",".","."],
         ["",".",".",".",".","4","5",".","3"],
         ["","7",".","",".","",".",".","."],
         ["7","2",".",".","1",".",".","9","."],
         [".",".","4",".","",".","8",".","."],
         [".","9",".",".","8",".",".","1","2"],
         [".",".",".",".",".",".",".","2","."],
         ["2",".","7","8",".",".",".",".","."],
         [".",".","3",".","5",".","7","6","."]]
    solveSudoku(l)
    print(l)