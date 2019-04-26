def exist(board: [[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if find(board, word, i, j):
                    return True
    return False

#每次回退要删除改点的后续路径
def find(board:[[]], word:str, i:int, j:int):
    path = []
    gone = {}
    l = len(board[0])
    h = len(board)
    while True:
        if word[len(path)] == board[i][j]:
            path.append([i, j])
            if (i, j) not in gone.keys():
                gone[i, j] = []
            if len(path) == len(word):
                return True
            if i + 1 < h and (i + 1, j) not in gone[(i, j)] and [i + 1, j] not in path:
                gone[(i, j)].append((i + 1, j))
                i = i + 1
            elif j + 1 < l and (i, j + 1) not in gone[(i, j)] and [i, j + 1] not in path:
                gone[(i, j)].append((i, j + 1))
                j = j + 1
            elif i - 1 >= 0 and (i - 1, j) not in gone[(i, j)] and [i - 1, j] not in path:
                gone[(i, j)].append((i - 1, j))
                i = i - 1
            elif j - 1 >= 0 and (i, j - 1) not in gone[(i, j)] and [i, j - 1] not in path:
                gone[(i, j)].append((i, j - 1))
                j = j - 1
            else:
                path.pop()
                if len(path) > 0:
                    [i, j] = path.pop()
                    olist = gone.get((i, j))
                    for o in olist:
                        if o in gone.keys():
                            gone.pop(o)
                else:
                    break
        else:
            if len(path) > 0:
                [i, j] = path.pop()
                olist = gone.get((i, j))
                for o in olist:
                    if o in gone.keys():
                        gone.pop(o)
            else:
                break
    return False

def minWindow(s: str, t: str) -> str:
    if len(t) == 1:
        if t in s:
            return t
    res = [[] for x in range(len(s))]
    res_min = len(s)
    min_str = ''
    for i in range(len(s)):
        for tt in t:
            if s[i] == tt:
                for j in range(i):
                    if len(res[j]) > 0 and s[i] not in res[j]:
                        res[j].append(s[i])
                        if len(res[j]) == len(t):
                            min_str_n = s[j: i + 1]
                            res_min_n = len(min_str_n)
                            if res_min > res_min_n:
                                res_min = res_min_n
                                min_str = min_str_n
                res[i].append(s[i])
                break
    return min_str


def combine(n: int, k: int) -> [[int]]:
    res = []
    result = [i + 1 for i in range(k)]
    i = k - 1
    cou = 1
    res.append(result[:])
    while i >= 0:
        if result[i] + cou <= n:
            if result[i] + cou not in result:
                result[i] += cou
                cou = 1
                if i == k - 1:
                    if result not in res:
                        res.append(result[:])
                else:
                    i += 1
            else:
                cou += 1
        else:
            i = i - 1
            cou = 1
            for j in range(i + 1, k):
                result[j] = 0
    return res


def combine2(n: int, k: int) -> [[int]]:
    res = []
    result = [i + 1 for i in range(k)]
    i = k - 1
    cou = 1
    res.append(result[:])
    while i >= 0:
        if result[i] + cou <= n:
            if result[i] + cou not in result:
                result[i] += cou
                cou = 1
                if i == k - 1:
                    if result not in res:
                        res.append(result[:])
                else:
                    i += 1
            else:
                cou += 1
        else:
            i = i - 1
            cou = 1
            for j in range(i + 1, k):
                result[j] = result[i]
    return res

def largestRectangleArea(heights:[int]) -> int:
    if len(heights) == 0:
        return 0
    left = 0
    right = len(heights) - 1
    max_q = max(min(heights[left: right + 1]) * (right - left + 1),heights[left], heights[right])
    if heights[left] > heights[right]:
        down = False
        pos = right
    else:
        down = True
        pos = left
    while left < right and pos >= left and pos <= right:
        if down:
            pos += 1
            if pos >= right:
                break
            if heights[pos] > min(heights[left: right + 1]):
                left = pos
                q =  max(min(heights[left: right + 1]) * (right - left + 1),heights[pos])
                if q > max_q:
                    max_q = q
                if heights[left] > heights[right]:
                    pos = right
                    down = not down
        else:
            pos -= 1
            if pos <= left:
                break
            if heights[pos] > min(heights[left: right + 1]):
                right = pos
                q = max(min(heights[left: right + 1]) * (right - left + 1),heights[pos])
                if q > max_q:
                    max_q = q
                if heights[right] > heights[left]:
                    pos = left
                    down = not down
    return max_q

def subsetsWithDup(nums: [int]) -> [[int]]:
    nums.sort()
    res_map = {}
    l = len(nums)
    res_map[len(nums)] = [nums]
    while l > 0:
        res_l = res_map[l]
        r = []
        for res_one in res_l:
            for j in range(l):
                res_copy = res_one[:]
                res_copy = res_copy[0: j] + res_copy[j + 1:]
                if res_copy not in r:
                    r.append(res_copy)
        l -= 1
        res_map[l] = r
    res = []
    for rs in list(res_map.values()):
        for r in rs:
            res.append(r)
    return res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root: TreeNode) -> [int]:
    if root == None:
        return []
    left_val = inorderTraversal(root.left)
    left_val.append(root.val)
    right_val = inorderTraversal(root.right)
    for val in right_val:
        left_val.append(val)
    return left_val

def evalRPN(tokens: [str]) -> int:
    nums = []
    for i in tokens:
        if i == '+':
            nums1 = nums.pop()
            nums2 = nums.pop()
            nums.append(nums2 + nums1)
        elif i == "-":
            nums1 = nums.pop()
            nums2 = nums.pop()
            nums.append(nums2 - nums1)
        elif i == "*":
            nums1 = nums.pop()
            nums2 = nums.pop()
            nums.append(nums2 * nums1)
        elif i == "/":
            nums1 = nums.pop()
            nums2 = nums.pop()
            nums.append(int(nums2 / nums1))
        else:
            nums.append(int(i))
    return nums[0]

if __name__ == '__main__':
    # board =   [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    # print(exist(board, word))
    # S = "ADOBECODEBANC"
    # T = "ABC"
    # S = "a"
    # T = "a"
    # print(minWindow(S, T))
    # print(combine2(4, 3))
    # nums = [5,5,1,7,1,1,5,2,7,6]
    # print(largestRectangleArea(nums))
    # print(subsetsWithDup([4,4,4,1,4]))
    nums = ["2", "1", "+", "3", "*"]
    print(evalRPN(nums))