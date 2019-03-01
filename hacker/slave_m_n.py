from math import factorial

INT = 15

def solve(n, m):
    if m == 1:
        return 1
    m = m - 1
    k, m_n = change_to(m, n)
    return m_n[0]

def change_to(m, n):
    a = [1]
    b = [1]
    for i in range(m):
        b = mult_t(b, ty_t(i + 1))
        a = mult_t(a, ty_t(m + n - i))

    # print(b, a)
    # print(div_t(a, b))
    return div_t(a, b)

def ty_t(a):
    res = []
    while a > INT:
        res.append(int(a % INT))
        a = int(a/INT)
    res.append(int(a))
    return res

#加
def add_t(a, b):
    l_a = len(a)
    l_b = len(b)
    mul = []
    c_i = 0
    for i in range(max(l_a, l_b)):
        if i >= l_a:
            v_a = 0
        else:
            v_a = a[i]
        if i >= l_b:
            v_b = 0
        else:
            v_b = b[i]
        c_i = v_a + v_b + int(c_i / INT)
        mul.append(c_i % INT)
    if c_i > INT:
        mul.append(int(c_i / INT))
    return mul

#乘
def mult_t(a, b):
    l_a = len(a)
    l_b = len(b)
    mul = [0]
    c_i = 0
    for i in range(l_a):
        for j in range(l_b):
            m_i = []
            c_i = a[i] * b[j]
            m_i.append(c_i % INT)
            if c_i > INT:
                m_i.append(int(c_i / INT))
            for k in range(i + j):
                m_i.insert(0, 0)
            mul = add_t(m_i, mul)
    if c_i > INT:
        mul.append(int(c_i/INT))
    return mul

#减
def sub_t(a, b):
    l_a = len(a)
    l_b = len(b)
    mul = []
    c_i = 0
    if l_b > l_a:
        return a, -1
    elif l_a == l_b:
        for i in range(l_b - 1, -1, -1):
            if a[i] > b[i]:
                break
            elif a[i] < b[i]:
                return a, -1
    for i in range(max(l_a, l_b)):
        if i >= l_a:
            v_a = 0
        else:
            v_a = a[i]
        if i >= l_b:
            v_b = 0
        else:
            v_b = b[i]
        v_a = v_a + c_i
        if v_a >= v_b:
            mul.append(v_a - v_b)
            c_i = 0
        else:
            c_i = -1
            mul.append(v_a - v_b + INT)
    return mul, 1

#除
def div_t(a, b):
    l_a = len(a)
    l_b = len(b)
    if l_b > l_a:
        return 0, a
    elif l_a == l_b:
        for i in range(l_b - 1, -1, -1):
            if a[i] > b[i]:
                break
            elif a[i] < b[i]:
                return 0, a

    res = []

    for i in range(INT):
        b_i = mult_t([i], b)
        s_i, big = sub_t(a[0 - l_b: ], b_i)
        if big == -1:
            res.append(i - 1)
            b_i = mult_t([i - 1], b)
            if i > 1:
                s_i, big = sub_t(a[0 - l_b:], b_i)
            else:
                s_i = a[0 - l_b:]
            break
    for k in range(l_a - l_b):
        for i in range(len(s_i) - 1, -1, -1):
            if s_i[i] == 0:
                s_i.pop()
            else:
                break
        s_i.insert(0, a[l_a - l_b - k - 1])
        # print(s_i)
        for i in range(INT):
            b_i = mult_t([i], b)
            s_i_t, big = sub_t(s_i, b_i)
            if big == -1:
                res.insert(0, i - 1)
                b_i = mult_t([i - 1], b)
                s_i, big = sub_t(s_i, b_i)
                break
    return res, s_i



if __name__ == '__main__':
    # for n in range(1, 20):
    #     for m in range(1, 11):
    #         print(solve(n, m))
    # for i in range(10, 20):
    #     if factorial(i) > 1000000007:
    #         print(i)
    #         break
    print(solve(522, 575))
    # a = [2, 12]
    # b = [10, 5]
    # print(mult_t(b, [2]))
    # print(div_t(a, b))
    # print(div_t([0, 0, 0, 12], [0, 1, 0 ,3]))
    # print(ty_t(24*23*22*21))
    # print(ty_t(1*2*3*4))
    # print(ty_t(24*23*22*21/(1*2*3*4)))