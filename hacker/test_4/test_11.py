DEFAULT_MAX = 99999
def jump(nums:[int]) -> int:
    l = len(nums)
    res = [[DEFAULT_MAX for i in range(l)] for i in range(l)]
    res[0][0] = 0
    for i in range(l):
        if i == 0:
            for j in range(1, nums[i] + 1):
                if j >= l:
                    break
                res[i][j] = 1
        else:
            min = DEFAULT_MAX
            for k in range(i):
                if min > res[k][i]:
                    min = res[k][i]
            if min == DEFAULT_MAX:
                break
            else:
                for m in range(1, nums[i] + 1):
                    if i + m >= l:
                        break
                    res[i][i + m] = min + 1
    min = DEFAULT_MAX
    for i in range(l):
        if min > res[i][l - 1]:
            min = res[i][l - 1]
    return min


def jump2(nums:[int]) -> int:
    if len(nums) <= 1:
        return 0
    start = 0
    end = nums[start] + start
    ju = 0
    while True:
        if end >= len(nums) - 1:
            ju += 1
            break
        else:
            m = 0
            pos = 0
            for i in range(start + 1, end + 1):
                if nums[i] + i >= m:
                    m = i + nums[i]
                    pos = i
            start = pos
            end = nums[start] + start
            ju += 1
    return ju

if __name__ == '__main__':
    # listInt = [1 for i in range(1, 1000000)]
    listInt = [10,9,8,7,6,5,4,3,2,1,1,0]
    print(jump2(listInt))
