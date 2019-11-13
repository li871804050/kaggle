def isMatch2(s: str, p: str) -> bool:
    m = [[0 for x in range(len(s) + 1)] for y in range(len(p) + 1)]
    m[0][0] = 1
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            for k in range(len(s) + 1):
                if m[i - 1][k] == 1:
                    m[i][k] = 1
                    for j in range(k, len(s) + 1):
                        m[i][j] = 1
        else:
            for j in range(len(s)):
                if m[i - 1][j] == 1:
                    if p[i - 1] == '?' or p[i - 1] == s[j]:
                        m[i][j + 1] = 1

    if m[len(p)][len(s)] == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    a = 'abcde'
    b = 'a*e'
    print(isMatch2(a, b))