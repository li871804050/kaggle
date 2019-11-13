class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if target not in nums:
            return [-1, -1]
        ind = nums.index(target)
        nums_new = nums[::-1]
        ind2 = nums_new.index(target)
        return [ind, len(nums) - ind2 - 1]

    def searchInsert(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[right] < target:
            return right + 1
        elif nums[left] >= target:
            return left
        return left + 1

    def isValidSudoku(self, board: [[str]]) -> bool:
        for i in range(len(board[0])):
            if not self.findOneValid1(board, i):
                return False
        for j in range(len(board)):
            if not self.findOneValid2(board, j):
                return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not self.findOneValid3(board, i, j):
                    return False
        return True

    def findOneValid1(self, board:[[str]], i: int):
        all_num = []
        for j in range(len(board)):
            if board[j][i] in all_num:
                return False
            elif board[j][i] != '.':
                all_num.append(board[j][i])

        return True

    def findOneValid2(self, board:[[str]], j: int):
        all_num = []
        for i in range(len(board[0])):
            if board[j][i] in all_num:
                return False
            elif board[j][i] != '.':
                all_num.append(board[j][i])

        return True

    def findOneValid3(self, board:[[str]], i: int, j: int):
        all_num = []
        for m in range(3):
            for n in range(3):
                if board[i + m][j + n] in all_num:
                    return False
                elif board[i + m][j + n] != '.':
                        all_num.append(board[i + m][j + n])
        return True

if __name__ == '__main__':
    solution = Solution()
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    # print(solution.searchRange(nums, target))
    # nums = [1]
    # target = 1
    # print(solution.searchInsert(nums, target))
    board = [["7",".",".",".","4",".",".",".","."],[".",".",".","8","6","5",".",".","."],[".","1",".","2",".",".",".",".","."],[".",".",".",".",".","9",".",".","."],[".",".",".",".","5",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    print(solution.isValidSudoku(board))