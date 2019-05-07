import re
def minSubArrayLen(s: int, nums: [int]) -> int:
    sum_list = []
    res = []
    k = 0
    for i in range(len(nums)):
        if nums[i] >= s:
            return 1
        else:
            sum_list.append(nums[i])
        for j in range(len(sum_list) - 2, k - 1, -1):
            if sum_list[j] + nums[i] >= s:
                res.append(i - j + 1)
                k += 1
                break
            elif sum_list[j] + nums[i] < s:
                sum_list[j] += nums[i]
            else:
                k += 1

    if len(res) > 0:
        return min(res)
    return 0

def minSubArrayLen(s: int, nums: [int]) -> int:
    left, right, res = 0, len(nums), 0
    while left <= right:
        mid = (left + right) // 2  # 滑动窗口大小
        if helper(mid, nums, s):  # 如果这个大小的窗口可以那么就缩小
            res = mid
            right = mid - 1
        else:  # 否则就增大窗口
            left = mid + 1
    return res


class WordDictionary:

    def __init__(self):
        self.data = '  '

    def addWord(self, word: str) -> None:
        self.data += word + ' '

    def search(self, word: str) -> bool:
        print('.* ' + word + ' .*')
        if re.match('.* ' + word + ' .*', self.data):
            return True
        else:
            return False

def helper(size, nums, s):
    sum_size = 0
    for i in range(len(nums)):
        sum_size += nums[i]
        if i >= size:
            sum_size -= nums[i - size]
        if sum_size >= s:
            return True
    return False


if __name__ == '__main__':
    # s = 15
    # nums = [1, 2, 3, 4, 5]
    # print(minSubArrayLen(s, nums))
    wordDic = WordDictionary()
    add = ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
    sea = [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
    for a in add:
        wordDic.addWord(a)
    for s in sea:
        if len(s) > 0:
            print(wordDic.search(s[0]))
        else:
            print(False)