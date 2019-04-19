def generateParenthesis(n: int) -> [str]:
        res = []
        res.append([''])
        res.append(['()'])
        for i in range(1, n + 1):
            res_i = []
            for k in range(i):
                 for r1 in res[i]:
                     for r2 in res[i - k]:
                         r = r1 + r2
                         res_i.append(r)
            res.append(res_i)
        return res[n]


def removeDuplicates(nums: [int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    i = 1
    pos = []
    p = 0
    while True:
        if i >= len(nums):
            break
        if nums[i] in nums[0: p + 1]:
            pos.insert(0, i)
        else:
            if len(pos) > 0:
                p = pos.pop()
                nums[p] = nums[i]
                pos.insert(0, i)
            else:
                p += 1
        i += 1
    print(nums)
    if len(pos) == 0:
        return i
    return p + 1

if __name__ == '__main__':
    # print(generateParenthesis(3))
    l = [0,0]
    print(removeDuplicates(l))