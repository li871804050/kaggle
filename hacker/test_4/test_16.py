def largestNumber(nums: [int]) -> str:
    l = len(nums)
    for i in range(l- 1):
        for j in range(i, l):
            if com(nums[i], nums[j]) == 2:
                num = nums[j]
                nums[j] = nums[i]
                nums[i] = num
    s = ''
    for n in nums:
        s = s + str(n)
    return str(int(s))

def com(a, b):
    if a == b:
        return 1, 0
    a = str(a)
    b = str(b)
    for i in range(min(len(a),len(b))):
        if int(a[i]) > int(b[i]):
            return 1
        elif int(a[i]) < int(b[i]):
            return 2
    if int(b) > int(a):
        return com(a, int(b[len(a): ]))
    elif int(b) < int(a):
        return com(int(a[len(b):]), b)


if __name__ == '__main__':
    print(largestNumber([0, 0]))