import math
def addBinary(a: str, b: str) -> str:
    ab = 0
    la = len(a) - 1
    lb = len(b) - 1
    s = ''
    while la >= 0 or lb >= 0:
        if la >= 0:
            ab += int(a[la])
            la -= 1
        if lb >= 0:
            ab += int(b[lb])
            lb -= 1
        s = str(ab % 2) + s
        ab = int(ab / 2)
    s = str(ab) + s
    return s

def fullJustify(words: [str], maxWidth: int) -> [str]:
    res = []
    lines = []
    i = 0
    countWord = 0
    while i < len(words):
        if (countWord > 0 and countWord + len(words[i]) + 1 > maxWidth):
            res.append(getLine(maxWidth, countWord, lines, i == len(words)))
            lines = []
            countWord = len(words[i])
            lines.append(words[i])
        else:
            if countWord != 0:
                countWord += 1
            countWord += len(words[i])
            lines.append(words[i])
        i += 1
    if len(lines) != 0:
        res.append(getLine(maxWidth, countWord, lines, i == len(words)))
    return res


def getLine(maxWidth, countWord, lines, last):
    if len(lines) > 1:
        space = int((maxWidth - countWord) / (len(lines) - 1)) + 1
        moreSpace = int((maxWidth - countWord) % (len(lines) - 1))
    else:
        line = lines[0]
        for i in range(maxWidth - countWord):
            line += ' '
        return line
    line = ''
    if not last:
        for i in range(len(lines)):
            if i == 0:
                line += lines[i]
            else:
                l = space
                if i <= moreSpace:
                    l += 1
                for j in range(l):
                    line += ' '
                line += lines[i]
    else:
        for i in range(len(lines)):
            if i == 0:
                line += lines[i]
            else:
                line += ' ' + lines[i]
        for j in range(len(line), maxWidth):
            line += ' '
    return line

def mySqrt(x: int) -> int:
    return int(math.sqrt(x))

def simplifyPath(path: str) -> str:
    paths = path.split("/")
    r_p = []
    for p in paths:
        if p == '.' or p == '':
            continue
        elif p == '..' and len(r_p) > 0:
            r_p.pop()
        else:
            r_p.append(p)
    if len(r_p) == 0:
        return '/'
    else:
        s = ''
        for p in r_p:
            s += '/' + p
        return s

def setZeroes(matrix: [[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(matrix):
        for j in range(matrix[0]):
            if matrix[i][j] == 0:
                for x in range(matrix):
                    if matrix[x][j] != 0:
                        matrix[x][j] = None
                for y in range(matrix[0]):
                    if matrix[i][y] != 0:
                        matrix[i][y] = None
    for i in range(matrix):
        for j in range(matrix[0]):
            if matrix[i][j] == None:
                matrix[i][j] = 0


def searchMatrix(matrix:[[int]], target: int) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    h = len(matrix)
    l = len(matrix[0])
    start = int((h * l)/2)
    left = 0
    right = h * l
    while True:
        if matrix[int(start/l)][start%l] == target:
            return True
        elif matrix[int(start/l)][start%l] > target:
            right = start
            if start == int((left + start) / 2):
                break
            start = int((left + start)/2)
        else:
            left = start
            if start == int((right + start)/2):
                break
            start = int((right + start)/2)
    return False

def sortColors(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.insert(0, 0)
            nums = nums[0: i + 1] + nums[i + 2:]
            i += 1
        elif nums[i] == 2:
            nums.insert(len(nums), 2)
            nums = nums[0: i] + nums[i + 1:]
            for j in range(i, len(nums)):
                if nums[i] == 2:
                    i += 1
                else:
                    break
        else:
            i += 1

def findMoreNum(nums:[int]):
    num = 0
    count = 0
    for i in range(0, len(nums)):
        if count == 0:
            num = nums[i]
            count += 1
        else:
            if num == nums[i]:
                count += 1
            else:
                count -= 1
    return num

if __name__ == '__main__':
    # words = ["Listen","to","many,","speak","to","a","few."]
    # maxWidth = 6
    # print(fullJustify(words, maxWidth))
    # matrix = [
    #     [10]
    # ]
    # target = 10
    # print(searchMatrix(matrix, target))
    color = [0, 2, 1, 2, 1, 0, 2, 2, 2, 1]
    # sortColors(color)
    # print(color)
    print(findMoreNum(color))