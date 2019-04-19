def rob(nums:[int]) -> int:
    if len(nums) == 0:
        return 0
    res = [0 for i in range(len(nums))]
    l = len(nums) - 1
    for i in range(l + 1):
        if i == 0:
            res[l - i] = nums[l - i]
        elif i == 1:
            res[l - i] = max(res[l - i + 1], nums[l - i])
        elif i == 2:
            res[l - i] = max(res[l - i + 1], nums[l - i] + res[l - i + 2])
        else:
            res[l - i] = max(res[l - i + 1], nums[l - i] + res[l - i + 2], nums[l - i] + res[l - i + 3])
    return res[0]

if __name__ == '__main__':
    s = [2, 7, 9, 3, 1, 8, 7, 4]
    print(rob(s))