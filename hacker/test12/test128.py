class Solution:
    #数组过长使用 方法1
    #数组最大最小值差距太大 方法2
    def longestConsecutive(self, nums: [int]) -> int:
        if len(nums) < 2:
            return len(nums)
        min_num  = min(nums)
        max_num = max(nums)
        if max_num - min_num < len(nums):
            node = [0 for i in range(min_num, max_num + 1)]
            for num in nums:
                node[num - min_num] = 1
            node_str = str(node).replace(",", "").replace("[", "").replace("]", "").replace(" ", "")
            strs = node_str.split("0")
            res = [len(s) for s in strs]
            return max(res)
        else:
            result = []
            for num in nums:
                r = []
                k = 0
                same = False
                while k < len(result):
                    if num in result[k]:
                        same = True
                        break

                    if (num - 1 in result[k] or num + 1 in result[k]):
                        for kk in result[k]:
                            r.append(kk)
                        result.remove(result[k])
                    else:
                        k = k + 1
                if not same:
                    r.append(num)
                    result.append(r)

            re = [len(r) for  r in result]
            return max(re)

if __name__ == '__main__':
    nums = [0,0,-1]
    s = Solution()
    print(s.longestConsecutive(nums))
