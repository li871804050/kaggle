import math
def numDecodings(s: str) -> int:
    res = []
    for i in range(len(s)):
        if i == 0:
            if s[i] == '0':
                return 0
            res.append(1)
        else:
            s_ = s[i - 1] + s[i]
            if int(s_) <= 26 and int(s_) > 10 and int(s_) != 20:
                if i == 1:
                    res.append(res[i - 1] + 1)
                else:
                    res.append(res[i - 1] + res[i - 2])
            elif s[i] == '0':
                if s[i - 1] != '1' and s[i - 1] != '2':
                    return 0
                if i == 1:
                    res.append(1)
                else:
                    res.append(res[i - 2])
            else:
                res.append(res[i - 1])
    return res[-1]

def reverseWords(s: str) -> str:
    words = s.split(' ')
    s_ = ''
    for i in range(len(words) - 1, -1, -1):
        if words[i] != '':
            if s_ == '':
                s_ = words[i]
            else:
                s_ += ' ' + words[i]
    return s_

def maxProduct(nums:[int]) -> int:
    max_res = []
    min_res = []
    for i in range(len(nums)):
        if i == 0:
            max_res.append(nums[i])
            min_res.append(nums[i])
        else:
            if nums[i] < 0:
                max_res.append(max(min_res[i - 1]*nums[i], nums[i]))
                min_res.append(min(max_res[i - 1]*nums[i], nums[i]))
            else:
                max_res.append(max(max_res[i - 1]*nums[i], nums[i]))
                min_res.append(min(min_res[i - 1]*nums[i], nums[i]))
    return max(max_res)

def findMin(nums:[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    i = 0
    while True:
        if len(nums) + i < 0:
            return nums[i]
        if nums[i] < nums[i - 1]:
            return nums[i]
        i -= 1

def twoSum(numbers:[int], target: int) -> [int]:
    for i in range(len(numbers)):
        ind = target - numbers[i]
        print(numbers[i + 1:])
        if ind in numbers[i + 1:]:
            return i + 1, numbers[i + 1:].index(ind) + 2 + i

def trailingZeroes(n: int) -> int:
    lo = int(math.log(n, 5))
    count = 0
    for i in range(lo, -1, -1):
        count += int(n/pow(5, i))*((pow(5, i) - 1)/4)
        n = n % pow(5, i)
        if n < 5:
            break

    return int(count)


if __name__ == '__main__':
    # nums = "20626"
    # print(numDecodings(nums))
    # s = "the sky is blue"
    # print(reverseWords(s))
    # nums = [-2,3,-4]
    # print(maxProduct(nums))
    # nums = [2,2,2,0,1]
    # print(findMin(nums))
    # num = [0, 0, 3, 4]
    # target = 0
    # print(twoSum(num, target))
    print(trailingZeroes(100))