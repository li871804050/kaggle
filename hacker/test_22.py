def lengthOfLongestSubstring(s: str) -> int:
    max_str = [1 for i in range(len(s))]

    for i in range(1, len(s)):
        l = max_str[i - 1]
        for k in range(i - l, i):
            if s[k] == s[i]:
                l = i - k - 1
                break
        max_str[i] = l + 1
    return max(max_str)

def longestPalindrome(s: str) -> str:
    long_p = [1 for i in range(len(s))]
    for i in range(1, len(s)):
        if long_p[i - 1] > 1 and i - long_p[i - 1] - 1 >= 0:
            if s[i] == s[i - long_p[i - 1] - 1]:
                long_p[i] = long_p[i - 1] + 2
            else:
                long_p[i] = find_max(s, i - long_p[i - 1] - 1, i)
        else:
            if i - long_p[i - 1] - 1 < 0:
                long_p[i] = find_max(s, 0, i)
            else:
                long_p[i] = find_max(s, max(0, i - 3), i)
    m = max(long_p)
    ind = long_p.index(m)

    return s[ind - m + 1: ind + 1]

def find_max(s, i, j):
    l = i
    r = j
    cou = 0
    while True:
        if l <= r and s[l] == s[r]:
            if l == r:
                cou += 1
            else:
                cou += 2
            l += 1
            r -= 1
        else:
            i += 1
            l = i
            r = j
            cou = 0
        if l > r and cou > 0:
            break
        if i > j:
            break
    return cou

def convert(s: str, numRows: int) -> str:
    lonZ = 2*numRows - 2
    numZ = int(len(s) / lonZ)
    res = ''
    for i in range(numRows):
        for j in range(numZ + 1):
            if i + lonZ * j < len(s):
                print(i + lonZ * j)
                res += s[i + lonZ * j]
            if i > 0 and i < numRows - 1:
                if lonZ*j + lonZ - i < len(s):
                    print(lonZ*j + lonZ - i)
                    res += s[lonZ*j + lonZ - i]
    return res

def reverse(x: int) -> int:
    x = str(x)
    i = 0
    l = len(x)
    s = ['' for i in range(l)]
    if x[0] == '-':
        i += 1
        l += 1
        s[0] = '-'
    while True:
        r = l - i - 1
        if i == r:
            s[i] = x[i]
            break
        elif i > r:
            break
        s[r] = x[i]
        s[i] = x[r]
        i += 1
    ss = ''
    for i in s:
        ss += i
    return int(ss)

def myAtoi(str: str) -> int:
        s = ''
        for i in range(len(str)):
            if str[i] == ' ' and s == '':
                continue
            if s == '':
                s = str[i]
                if s != '-' and (s < '0' or s > '9'):
                    return 0
                continue
            if str[i] >= '0' and str[i] <= '9':
                s += str[i]
            else:
                break
        s = int(s)
        if s > 2147483648 or s < -2147483647:
            return 0
        return s

def isMatch(s: str, p: str) -> bool:
    m = [[0 for x in range(len(s) + 1)] for y in range(len(p) + 1)]
    m[0][0] = 1
    for i in range(len(p)):
        if p[i] == '*':
            for k in range(len(s) + 1):
                if m[i][k] == 1:
                    m[i + 1][k] = 1
            for k in range(len(s) + 1):
                if m[i + 1][k] == 1:
                    for j in range(k, len(s)):
                        if p[i - 1] == s[j] or p[i - 1] == '.':
                            m[i + 1][j + 1] = 1
                        else:
                            break
            if i - 1 >= 0:
                for k in range(len(s) + 1):
                    if m[i - 1][k] == 1:
                        m[i + 1][k] = 1
        else:
            for j in range(len(s)):
                if m[i][j] == 1:
                    if p[i] == '.' or p[i] == s[j]:
                        m[i + 1][j + 1] = 1

    if m[len(p)][len(s)] == 1:
        return True
    else:
        return False

def maxArea(height: [int]) -> int:
    if len(height) < 2:
        return 0
    squre = 0
    for j in range(len(height) - 1):
        for i in range(j, len(height)):
            s = (i - j) * min(height[j], height[i])
            if s > squre:
                squre = s
    return squre

def maxArea2(height: [int]) -> int:
    if len(height) < 2:
        return 0
    right = len(height) - 1
    left = 0
    squer = (right - left)*min(height[right], height[left])
    l_or_r = False
    if height[right] > height[left]:
        l_or_r = True
    while right > left:
        q = min(height[right], height[left]) * (right - left)
        if squer < q:
            squer = q
            if height[right] > height[left]:
                l_or_r = True
            else:
                l_or_r = False
        if l_or_r:
            left += 1
        else:
            right -= 1
    return squer




if __name__ == '__main__':
    # s = "qooooor"
    # # l = lengthOfLongestSubstring(s)
    # # print(l)
    # print(longestPalindrome(s))
    # print(longestPalindrome("bananas"))
    # print(convert("LEETCODEISHIRING", 3))
    # print(reverse(10))
    # print(myAtoi('3234adws'))
    a = "mississippi"
    b = "mis*is*p*."
    # a =  "aab"
    # b =  "c*a*b"
    # print(isMatch(a, b))
    print(maxArea2([2,3,4,5,18,17,6]))