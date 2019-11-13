# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        nodes = []
        node = root
        while node != None:
            right = node.right
            left = node.left
            node.left = right
            node.right = left
            if right != None:
                nodes.append(right)

            if left != None:
                node = left
            else:
                if len(nodes) > 0:
                    node = nodes.pop()
                else:
                    break
        return root

    def calculate(self, s: str) -> int:
        pos = 0
        nums = []
        op = []
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
                op.append(s[i])
                nums.append(int(s[pos: i]))
                pos = i + 1
        nums.append(int(s[pos:]))
        i = 0
        while i < len(op):
            if op[i] == '*':
                nums[i] = nums[i] * nums[i + 1]
                nums.pop(i + 1)
                op.pop(i)
            elif op[i] == '/':
                nums[i] = int(nums[i] / nums[i + 1])
                nums.pop(i + 1)
                op.pop(i)
            else:
                i += 1
        result = 0
        if len(nums) > 0:
            result = nums[0]
        for i in range(len(op)):
            if op[i] == '+':
                result += nums[i + 1]
            elif op[i] == '-':
                result -= nums[i + 1]
        return result

    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i: k + i]))
        return res

    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        l = len(matrix)
        h = len(matrix[0])
        if l > 1 and h > 1:
            for i in range(min(l, h)):
                if matrix[i][i] >= target:
                    break
            m = i
            n = i
            while m >= 0 and n < h:
                if matrix[m][n] == target:
                    return True
                if matrix[m][n] > target:
                    m = m - 1
                else:
                    n = n + 1

            m = i
            n = i
            while m < l and n >= 0:
                if matrix[m][n] == target:
                    return True
                if matrix[m][n] > target:
                    n = n - 1
                else:
                    m = m + 1

        else:
            if l == 1:
                for i in range(h):
                    if matrix[0][i] == target:
                        return True
            elif h == 1:
                for i in range(l):
                    if matrix[i][0] == target:
                        return True
        return False

    def binaryTreePaths(self, root: TreeNode) -> [str]:
        if root == None:
            return []
        res = []
        nodes = []
        path = {}
        path[root] = [root.val]
        while root != None:
            if root.right == None and root.left == None:
                res.append(path[root])

            if root.right != None:
                nodes.append(root.right)
                list = path[root][:]
                list.append(root.right.val)
                path[root.right] = list
            if root.left != None:
                nodes.append(root.left)
                list = path[root][:]
                list.append(root.left.val)
                path[root.left] = list
                root = root.left
            else:
                if len(nodes) > 0:
                    root = nodes.pop()
                else:
                    break
        res_str = []
        for r in res:
            s = ''
            for j in r:
                s += str(j) + '->'
            s = s[:-2]
            if s not in res_str:
                res_str.append(s)
        return res_str

    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        pox2 = 0
        pox3 = 0
        pox5 = 0
        m = 1
        for i in range(1, n):
            m = min(res[pox2]*2, res[pox3]*3, res[pox5]*5)
            if m == res[pox2]*2:
                pox2 += 1
            if m == res[pox3]*3:
                pox3 += 1
            if m == res[pox5]*5:
                pox5 += 1
            res.append(m)
        return m


if __name__ == '__main__':
    solution = Solution()
    # s = '3+2*2'
    # print(solution.calculate(s))
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    # print(solution.maxSlidingWindow(nums, k))
    # mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    # target = 26
    # print(solution.searchMatrix(mat, target))
    print(solution.nthUglyNumber(10))