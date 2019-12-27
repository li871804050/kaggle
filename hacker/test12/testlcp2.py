class Solution:
    def fraction(self, cont: [int]) -> [int]:
        b = None
        l = len(cont) - 1
        for i in range(len(cont)):
            b = self.fraction2(cont[l - i], b)
        return b


    def fraction2(self, a, b:[]) -> [int]:
        if b is None:
            return [a, 1]
        return [a*b[0] + b[1], b[0]]

if __name__ == '__main__':
    s = Solution()
    cont = [0, 0, 3]
    print(s.fraction(cont))