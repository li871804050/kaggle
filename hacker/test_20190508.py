class Solution:
    def intToRoman(self, num: int) -> str:
        type = 1
        res = ''
        while num > 0:
            r = (num % 10)
            num = num // 10
            res = self.getOneNumber(r, type) + res
            type *= 10
        return res

    def getOneNumber(self, num, type):
        if num == 0:
            return ''
        first, five, ten = self.getType(type)
        if num >= 1 and num < 4:
            s = ''
            for i in range(num):
                s += first
            return s
        elif num ==4:
            return first + five
        elif num >= 5 and num < 9:
            s = five
            for i in range(num - 5):
                s += first
            return s
        elif num == 9:
            return first + ten


    def getType(self, nums):
        if nums < 10:
            return 'I', 'V', 'X'

        if nums < 100:
            return 'X', 'L', 'C'

        if nums < 1000:
            return 'C', 'D', 'M'

        return 'M', 'M','M'

    def romanToInt(self, s: str) -> int:
        result = 0
        last = -1
        for w in s:
            val = self.getOne(w)
            result += val
            if last > -1:
                if val > last:
                    result  = result - last - last
            last = val
        return result


    def getOne(self, w):
        if w == 'I':
            return 1
        if w == 'V':
            return 5
        if w == 'X':
            return 10
        if w == 'L':
            return 50
        if w == 'C':
            return 100
        if w == 'D':
            return 500
        if w == 'M':
            return 1000

    def threeSumClosest(self, nums: [int], target: int) -> int:
        m = 0
        nums.sort()
        t = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                sub = target - s
                if sub == 0:
                    return target
                if sub < 0:
                    right -= 1
                else:
                    left += 1
                sub = abs(sub)
                if m == 0:
                    m = sub
                    t = s
                elif sub < m:
                    m = sub
                    t = s

        return t

    def letterCombinations(self, digits: str) -> [str]:
        res = []
        for i in digits:
            ch = self.getNumToChar(i)
            if len(ch) > 0:
                if len(res) == 0:
                    res = ch
                else:
                    res_n = []
                    for x in res:
                        for c in ch:
                            res_n.append(x + c)
                    res = res_n[:]
        return res

    def getNumToChar(self, num: str):
        if num == '2':
            return ['a', 'b', 'c']
        if num == '3':
            return ['d', 'e', 'f']
        if num == '4':
            return ['g', 'h', 'i']
        if num == '5':
            return ['j', 'k', 'l']
        if num == '6':
            return ['m', 'n', 'o']
        if num == '7':
            return ['p', 'q', 'r', 's']
        if num == '8':
            return ['t', 'u', 'v']
        if num == '9':
            return ['w', 'x', 'y', 'z']
        return []

    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        res = []
        j = 0
        while j < len(nums) - 3:
            i = j + 1
            while i < len(nums) - 2:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[j] + nums[i] + nums[left] + nums[right]
                    sub = target - s
                    if sub == 0:
                        res.append([nums[j], nums[i], nums[left], nums[right]])
                        k = 1
                        while right - k > left:
                            if nums[left + k] == nums[left]:
                                k += 1
                            else:
                                break
                        left += k
                        k = 1
                        while right - k > left:
                            if nums[right - k] == nums[right]:
                                k += 1
                            else:
                                break
                        right -= k
                    if sub < 0:
                        k = 1
                        while right - k > left:
                            if nums[right - k] == nums[right]:
                                k += 1
                            else:
                                break
                        right -= k
                    elif sub > 0:
                        k = 1
                        while right - k > left:
                            if nums[left + k] == nums[left]:
                                k += 1
                            else:
                                break
                        left += k

                k = 1
                while i + k < len(nums) - 2:
                    if nums[i] == nums[i + k]:
                        k += 1
                    else:
                        break
                i += k
            k = 1
            while j + k < len(nums) - 3:
                if nums[j] == nums[j + k]:
                    k += 1
                else:
                    break
            j += k
        return res

if __name__ == '__main__':
    solution = Solution()
    # print(solution.intToRoman(10))
    # print(solution.romanToInt("LVIII"))
    # nums = [0,2,1,-3]
    # target = 1
    # print(solution.threeSumClosest(nums, target))
    # print(solution.letterCombinations('23'))
    nums = [-4,-3,-2,-1,0,0,1,2,3,4]
    target = 0
    print(solution.fourSum(nums, target))