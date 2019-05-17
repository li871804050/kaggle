class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 1
        #存在大于原数组长度的数，必定前面的数组中存在下雨数组长度的数，故只需要原数组长度的数即可
        res_pos = [-1 for x in range(len(nums))]
        for n in nums:
            if n > 0 and n <= len(nums):
                res_pos[n - 1] = 1
        if -1 not in res_pos:
            return len(res_pos) + 1
        return res_pos.index(-1) + 1

    def trap(self, height: [int]) -> int:
        if len(height) <= 1:
            return 0
        start = 0
        res = 0
        while start < len(height):
            if height[start] > 0:
                break
            else:
                start += 1
        h = 0
        while start < len(height):
            find = -1
            for i in range(start + 1, len(height)):
                if find == -1 and height[i] >= height[start]:
                    find = i
                elif find != -1 and height[i] > height[find]:
                    find = i
                elif find != -1 and height[i] < height[find]:
                    res += self.recken(height[start - h: find + 1])
                    start = find
                    find = -1
                    h = 0
            if height[start] > height[i]:
                start += 1
                h += 1
            else:
                if find == len(height) - 1:
                    res += self.recken(height[start - h: find + 1])
                break
        return res

    def recken(self, height: [int]):
        h = min(height[0], height[-1])
        s = 0
        for i in height:
            s += max(h - i, 0)
        return s

    def trap2(self, height: [int]) -> int:
        ans = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1,height[i])
            h2 = max(h2,height[-i-1])
            ans = ans + h1 + h2 -height[i]
        return  ans - len(height)*h1

    def trap3(self, height: [])-> int:
        if len(height) <= 1:
            return 0

        max_height = 0
        max_height_index = 0

        # 找到最高点
        for i in range(len(height)):
            h = height[i]
            if h > max_height:
                max_height = h
                max_height_index = i

        area = 0

        # 从左边往最高点遍历
        tmp = height[0]
        for i in range(max_height_index):
            if height[i] > tmp:
                tmp = height[i]
            else:
                area = area + (tmp - height[i])

        # 从右边往最高点遍历
        tmp = height[-1]
        for i in reversed(range(max_height_index + 1, len(height))):
            if height[i] > tmp:
                tmp = height[i]
            else:
                area = area + (tmp - height[i])
        return area

    def trap4(self, height: [])-> int:
        if len(height) <= 1:
            return 0
        height_max = max(height)
        height_max_index = height.index(height_max)
        area = 0
        m = height[0]
        for i in range(1, height_max_index):
            if height[i] > m:
                m = height[i]
            else:
                area += m - height[i]
        m = height[-1]
        for i in range(len(height) - 1, height_max_index, -1):
            if height[i] > m:
                m = height[i]
            else:
                area += m - height[i]
        return area


if __name__ == '__main__':
    solution = Solution()
    # nums = [1]
    # print(solution.firstMissingPositive(nums))
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [0,7,1,4,6]
    height = [2,8,5,5,6,1,7,4,5]
    print(solution.trap3(height), solution.trap4(height))
