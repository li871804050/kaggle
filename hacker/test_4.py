def turn_down(data):
    l = len(data)
    right = ''
    left = ''
    res = ''
    for i in range(l):
        if i == l - i - 1:
            res = right + str(data[i]) + ' ' + left[0: -1]
            break
        elif i > l - i - 1:
            res = right + left[0: -1]
            break
        else:
            right = right + str(data[l - i - 1]) + ' '
            left = str(data[i]) + ' ' + left
    return res

if __name__ == '__main__':
    data = [1, 3, 4, 6, 7]
    print(turn_down(data))