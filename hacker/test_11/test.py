class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        l = len(matrix[0])
        h = len(matrix)
        start = 0
        end = l * h - 1
        while start <= end:
            i = (start + end)//2
            l_1 = i // l
            h_1 = i % l
            if matrix[l_1][h_1] == target:
                return True
            else:
                if matrix[l_1][h_1] > target:
                    end = i - 1
                else:
                    start = i + 1
        return False



if __name__ == '__main__':
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    t = 13
    s = Solution()
    print(s.searchMatrix(m, t))