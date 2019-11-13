def claen(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == 'm' and s[i + 1] == 'i':
            s = s[: i] + s[i + 2:]
            i = max(0, i - 1)
        else:
            i = i + 1
    return s


if __name__ == '__main__':
    s = 'mmimiismsdf'
    print(claen(s))
    