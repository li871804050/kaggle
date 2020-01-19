class Solution:
    def constructArray(self, n: int, k: int) -> [int]:
        result = [i + 1 for i in range(n)]
        if n % 2 == 1 and k > 2:
            k = k - 1
        for j in range(1, k):
            t = result[j]
            result[j] = result[j + 1]
            result[j + 1] = t
        return result

if __name__ == '__main__':
    n = 3
    k = 2
    s = Solution()
    print(s.constructArray(n, k))