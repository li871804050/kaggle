def search(nums: [int], target: int) -> int:
    i = 0
    up = 0
    down = 0
    while i < len(nums):
        if i < 0:
            i = i + len(nums)
        if nums[i] == target:
            return i
        elif nums[i] > target:
            if nums[i] > nums[i - 1]:
                i = i - 1
                up = 1
            else:
                break
        else:
            if nums[i] < nums[(i + 1)%len(nums)]:
                i = (i + 1)%len(nums)
                down = 1
            else:
                break
        if down == 1 and up == 1:
            break
    return -1

def multiply(num1: str, num2: str) -> str:
    l1 = len(num1)
    l2 = len(num2)
    res = [0 for i in(range(l1 + l2))]
    for i in range(l1):
        for j in range(l2):
            s = int(num1[l1 - 1 - i])*int(num2[l2 - 1 - j])
            res[i + j] += s
    for i in range(len(res)):
        if res[i] >= 10:
            res[i + 1] += int(res[i]/10)
            res[i] = res[i] % 10

    start = 0
    l = l1 + l2 - 1
    result = ''
    for i in range(len(res)):
        if start == 0 and res[l - i] == 0:
            continue
        else:
            start = 1
            result += str(res[l - i])
    if '' == result:
        return '0'
    return result

def permute(nums: [int]) -> [[int]]:
    num = len(nums)
    res = [[] for x in range(num + 1)]
    res[1] = [[nums[0]]]
    for i in range(2, num + 1):
        r_i = []
        r_i_1 = res[i - 1]
        for k in range(len(r_i_1)):
            for j in range(i):
                r = r_i_1[k][:]
                r.insert(j, nums[i - 1])
                r_i.append(r)
        res[i] = r_i
    return res[i]


# def permute_int(num) -> [[int]]:
#     res = [[] for x in range(num + 1)]
#     res[1] = [[1]]
#     for i in range(2, num + 1):
#         r_i = []
#         r_i_1 = res[i - 1]
#         for k in range(len(r_i_1)):
#             for j in range(i):
#                 r = r_i_1[k][:]
#                 r.insert(j, i)
#                 r_i.append(r)
#         res[i] = r_i
#     return res[i]


def maxSubArray(nums:[int]) -> int:
    res = nums[:]
    for i in range(1, len(nums)):
        if res[i - 1] + nums[i] > res[i]:
            res[i] = res[i - 1] + nums[i]
    return max(res)

def spiralOrder(matrix: [[int]]) -> [int]:
    r_h = 0
    r_l = 0
    h = len(matrix) - 1
    l = len(matrix[0]) - 1
    if h == 0:
        return matrix[0]
    if l == 0:
        r = []
        for i in range(h + 1):
            r.append(matrix[i][0])
        return r
    i = 0
    j = 0
    res = []
    up = 0
    while True:
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            break
        res.append(matrix[i][j])
        if up == 0:
            j += 1
            if j == h:
                up = 1
                r_l += 1
        elif up == 1:
            i += 1
            if i == l:
                up = 2
                h -= 1
        elif up == 2:
            j -= 1
            if j == r_h:
                up = 3
                l -= 1
        elif up == 3:
            i -= 1
            if i == r_l:
                up = 0
                r_h += 1
        if l == r_l and h == r_h:
            res.append(matrix[i][j])
            res.append(matrix[l][h]);
            break
    return res

def spiralOrder2(matrix: [[int]]) -> [int]:
    ret = []
    if matrix == []:
        return ret
    ret.extend(matrix[0])  # 上侧
    new = [reversed(i) for i in matrix[1:]]
    if new == []:
        return ret
    r = spiralOrder([i for i in zip(*new)])
    ret.extend(r)
    return ret


if __name__ == '__main__':
    # nums = [4,5,6,7,0,1,2]
    # target = 3
    # print(search(nums, target))
    # num1 = "123"
    # num2 = "456"
    # print(multiply(num1, num2))
    # nums = [1, 2, 3]
    # print(permute(nums))
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # print(maxSubArray(nums))
    m = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
]
    # m =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder2(m))
    # m.reverse()
    # print(m)