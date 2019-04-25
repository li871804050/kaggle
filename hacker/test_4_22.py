def canJump(nums: [int]) -> bool:
    l = len(nums) - 1
    while l >= 0:
        for j in range(l - 1, -1, -1):
            if j + nums[j] >= l:
                l = j
                break
        if j == 0:
            break
    if l <= 0:
        return True
    return False

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals: [[]]) -> [[]]:
    start_int = []
    intervals_new = []
    for i in intervals:
        start_int.append(i[0])
    sort_start = sorted(start_int)
    interval = None
    for i in range(len(sort_start)):
        j = start_int.index(sort_start[i])
        start_int[j] = -1
        if interval == None:
            interval = intervals[j]
        else:
            interval_next = intervals[j]
            if interval[1] >= interval_next[0]:
                interval[1] = max(interval_next[1], interval[1])
            else:
                intervals_new.append(interval)
                interval = interval_next

    if interval != None:
        intervals_new.append(interval)
    return intervals_new

def insert(intervals: [[]], newInterval: []) -> [[]]:
    intervals_new = []
    for i in intervals:
        if newInterval == None:
            intervals_new.append(i)
        if newInterval[0] > i[1]:
            intervals_new.append(i)
            continue
        elif i[0] > newInterval[1] :
            intervals_new.append(newInterval)
            intervals_new.append(i)
            newInterval = None
            continue
        else:
            newInterval[0] = min(i[0], newInterval[0])
            newInterval[1] = max(i[1], newInterval[1])
    if newInterval != None:
        intervals_new.append(newInterval)
    return intervals_new

def getPermutation(n: int, k: int) -> str:
    res = []
    nums = [i  + 1for i in range(n)]
    fn = funcN(n)
    pos = n - 1
    while len(nums) > 0:
        num = int(k / fn[pos])
        k = k % fn[pos]
        if k == 0:
            res.append(nums.pop(num - 1))
            l = len(res)
            for num in nums:
                res.insert(l, num)
            break
        res.append(nums.pop(num))
        pos -= 1
        if k == 1:
            for n in nums:
                res.append(n)
            break
    s = ''
    for i in res:
        s += str(i)
    return s



def funcN(n):
    list = [1 for x in range(n + 1)]
    for i in range(1, n + 1):
        list[i] = list[i - 1]*i
    return list


if __name__ == '__main__':
    # nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    # print(canJump(nums))
    # nums = [[1,4],[1,5]]
    # print(merge(nums))
    # intervals = [[1, 3], [6, 9]]
    # newInterval = [2, 5]
    # print(insert(intervals, newInterval))
    # print(funcN(10))
    print(getPermutation(4, 9))