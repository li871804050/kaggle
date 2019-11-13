class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = []
        nodes = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == ')':
                if len(left) > 0:
                    pos = left.pop()
                    if len(nodes) == 0:
                        nodes.append([pos, i])
                    else:
                        for [x,y] in nodes:
                            if x == pos + 1 and y == i - 1:
                                nodes.remove([x, y])
                            elif y == pos - 1:
                                nodes.remove([x, y])
                                pos = x
                        nodes.append([pos, i])
        if len(nodes) > 0:
            l = [end - start + 1 for [start, end] in nodes]
            return max(l)
        return 0

    def nextPermutation(self, nums: [int]):
        find = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                find = True
                n_sort = self.getNext(nums[i - 1], nums[i - 1:])
                for j in range(i - 1, len(nums)):
                    nums[j] = n_sort[j - i + 1]
                break
        if not find:
            n_sort = nums[::-1]
            for i in range(len(nums)):
                nums[i] = n_sort[i]


    def getNext(self, first, nums):
        nums.sort()
        ind = nums.index(first)
        n = 1
        while ind < len(nums):
            if nums[ind + n] > first:
                break
            else:
                n += 1
        n += ind
        nums.insert(0, nums.pop(n))
        return nums

    def combinationSum3(self, candidates: [int], target: int) -> [[int]]:
        if target == 0:
            return []
        if len(candidates) == 0:
            return None
        candidates.sort()
        res = []
        times = target // candidates[0]
        rem = target % candidates[0]
        res_one = []
        for t in range(times):
            res_one.append(candidates[0])
        if rem == 0:
            res.append(res_one[:])
            rem = candidates[0]
            res_one.pop()
            times -= 1

        target = rem

        for t in range(1, times + 1):
            target +=candidates[0]
            res_one.pop()
            res_n = self.combinationSum(candidates[1:], target)
            if res_n != None:
                for r in res_n:
                    res.append(res_one[: times - t + 1] + r)
        return res

    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        return self.combinationSum3(candidates, target)

    def combinationSum3(self, candidates: [int], target: int) -> [[int]]:
        if len(candidates) == 0:
            return []
        if candidates[0] == target:
            return [[candidates[0]]]
        res = []
        res_n = self.combinationSum3(candidates[1:], target - candidates[0])
        res_n2 = self.combinationSum3(candidates[1:], target)
        if res_n != []:
            if len(res_n) == 0:
                res.append([candidates[0]])
            else:
                for r in res_n:
                    if [candidates[0]] + r not in res:
                        res.append([candidates[0]] + r)
        if res_n2 != None:
            for r in res_n2:
                if r not in res:
                    res.append(r)
        i = 0
        while i < len(res):
            if sum(res[i]) != target:
                res.pop(i)
            else:
                i += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    # print(solution.longestValidParentheses('()(())'))
    # nums = [1, 2, 3]
    # nums2 = [2, 3, 5]
    # print(nums + nums2)
    # nums = solution.nextPermutation(nums)
    # print(nums)
    # candidates = [2]
    # target = 1
    # print(solution.combinationSum(candidates, target))
    candidates = [10]
    target = 8
    print(solution.combinationSum2(candidates, target))