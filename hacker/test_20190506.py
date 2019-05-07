
#去掉后面不满足的
#反转比较
def shortestPalindrome(s: str) -> str:
    right = ''
    l = len(s)
    for i in range(l):
        if s[: l - i] == s[l - i -1:: -1]:
            break
        else:
            right += s[l - i - 1]
    return right + s

def shortest(s: str) -> str:
    n = len(s)
    for i in range(n - 1, -1, -1):
        print(s[0:i + 1], s[i::-1])
        if s[0:i + 1] == s[i::-1]:
            return s[-1:i:-1] + s
    return ""

def rob(nums: [int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    no_first = []
    has_first = []
    for i in range(len(nums)):
        if i == 0:
            has_first.append(nums[i])
            no_first.append(0)
        elif i == 1:
            no_first.append(nums[i])
            has_first.append(nums[i])
        elif i == 2:
            no_first.append(nums[i])
            has_first.append(has_first[0] + nums[i])
        else:
            has_first.append(max(has_first[i - 2], has_first[i - 3]) + nums[i])
            no_first.append(max(no_first[i - 2], no_first[i - 3]) + nums[i])
    has_first[len(nums) - 1] = 0
    return max(max(has_first), max(no_first))

def combinationSum3(k: int, n: int) -> [[int]]:
    return combination(k, n, 9)

def combination(k: int, n: int, m: int) -> [[int]]:
    if n <= 0:
        return None
    if k == 1:
        return [[n]]
    res_all = []
    for i in range(m, 1, -1):
        res = combination(k - 1, n - i, m - 1)
        if res != None:
            for re in res:
                if i > max(re):
                    re.append(i)
                    res_all.append(re)
    return res_all

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        list = []
        count = 0
        while root != None or len(list) > 0:
            count += 1
            if root.right != None:
                list.append(root.right)
            if root.left != None:
                root = root.left
            else:
                if len(list) > 0:
                    root = list.pop()
                else:
                    break
        return count

    def calculate(self, s: str) -> int:
        left_bracket = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                left_bracket.append(i)
            elif s[i] == ')':
                if len(left_bracket) == 0:
                    break
                pos = left_bracket.pop()
                formula_old = s[pos + 1: i]
                formula = self.cal(formula_old)
                if (i + 1 < len(s)):
                    s = s[: pos] + formula + s[i + 1:]
                    i = pos + len(formula) - 1
                else:
                    s = s[: pos] + formula
                    break
            i += 1
        res = int(self.cal(s))
        return res
    def cal(self, s:str):
        s = s.replace(' ', '')
        s = s.replace('(', '')
        s = s.replace(')', '')
        s = s.replace('--', '+')
        s = s.replace('+-', '-')
        pos = 0
        sum = 0
        op = '+'
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-':
                if op == '+':
                    if i != 0:
                        sum += int(s[pos: i])
                elif op == '-':
                    if i != 0:
                        sum -= int(s[pos: i])
                op = s[i]
                pos = i + 1
            if i == len(s) - 1:
                if op == '+':
                    sum += int(s[pos: i + 1])
                elif op == '-':
                    sum -= int(s[pos: i + 1])
        return str(sum)



if __name__ == '__main__':
    # print(shortest('abcd'))
    # s = 'abcd'
    # print(s[2: : -1], s[0:3])
    # nums = [2,1,2,6,1,8,10,10]
    # print(rob(nums))
    # print(combinationSum3(9, 45))
    s1 = "(5-(1+(5)))"
    s = Solution()
    print(s.calculate(s1))