class Solution:
    ##计算h[i]为最大长度的面积 需知道其前后小于h[i]的点m,n 面积=h[i]*(m -n - 1)
    def largestRectangleArea2(self, heights: [int]) -> int:
        q = []
        q.append(-1)
        area = 0
        for i in range(len(heights)):
            if heights[i] >= heights[q[-1]]:
                q.append(i)
            else:
                while len(q) > 1 and heights[q[-1]] > heights[i]:
                    pos = q.pop()
                    a = heights[pos]*(i - q[-1] - 1)
                    if area < a:
                        area = a
                q.append(i)
            if i == len(heights) - 1:
                while len(q) > 1:
                    pos = q.pop()
                    a = heights[pos]*(i - q[-1])
                    if area < a:
                        area = a
        return area

    def largestRectangleArea(self, heights: [int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        area = self.areas(heights)
        m = min(heights)
        pos = 0
        while True:
            pos_new = heights.index(m, pos)
            if pos_new == pos:
                break
            a = self.largestRectangleArea(heights[pos: pos_new])
            if a > area:
                area = a
            pos = pos_new
        if pos < len(heights):
            a = self.largestRectangleArea(heights[pos + 1: len(heights)])
            if a > area:
                area = a

        return area

    def areas(self, height) -> int:
        h = min(height)
        w = len(height)
        return h*w

if __name__ == '__main__':
    s = Solution()
    heigh = [6, 7, 5, 2, 4, 5, 9, 3]
    print(s.largestRectangleArea2(heigh))