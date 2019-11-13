def findRepeatedDnaSequences(s: str)->[]:
    res = []
    more = []
    for i in range(0, len(s) - 10):
        if s[i: i + 10] in res:
            continue
        for j in range(i + 1, len(s) - 9):
            if s[i: i + 10] == s[j: j + 10]:
                res.append(s[i: i + 10])
                break
    return more

def maxProfit2(k: int, prices: [int]) -> int:
    max_pf = {}
    for i in range(len(prices)):
        if prices[i] > prices[i - 1] and i > 0:
            continue
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > 0:
                if not i in max_pf:
                    max_pf[i] = {j: prices[j] - prices[i]}
                else:
                    max_pf[i][j] = prices[j] - prices[i]
                if prices[j] > prices[j - 1]:
                    if j - 1 in max_pf[i]:
                        max_pf[i].pop(j - 1)
    ma = 0
    res = {}
    for i in range(len(prices)):
        mx = get_one(max_pf, i, k, res)
        if ma < mx:
            ma = mx
    return ma



def get_one(max_pf, k, count, res):
    if count == 0:
        return 0
    ma = 0
    ke = None
    for key in max_pf.keys():
        if key >= k:
            if str(key) + '_' + str(count) in res:
                mx = res[str(key) + '_' + str(count)]
                if ma < mx:
                    ma = mx
                    ke = key
            else:
                map_key = max_pf[key]
                for i in map_key.keys():
                    if str(i) + '_' + str(count - 1) in res:
                        mx = res[str(key) + '_' + str(count)] +map_key[i]
                    else:
                        mx = map_key[i] + get_one(max_pf, i, count - 1, res)
                    if ma < mx:
                        ma = mx
                        ke = key
    res[str(ke) + '_' + str(count)] = ma
    return ma



def get_max(prices, i):
    pf = []
    res = []
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            pf.append(1)
        else:
            pf.append(-1)
    pf.append(-1)
    start = -1
    for i in range(len(prices)):
        if pf[i] == -1 and start >= 0:
            res.append(prices[i] - prices[start])
            start = -1
        if pf[i] == 1 and start < 0:
            start = i



def maxProfit(prices:[int]) -> int:
    pf = []
    res = []
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            pf.append(1)
        else:
            pf.append(-1)
    pf.append(-1)
    start = -1
    for i in range(len(prices)):
        if pf[i] == -1 and start >= 0:
            res.append(prices[i] - prices[start])
            start = -1

        if pf[i] == 1 and start < 0:
            start = i
    res.sort(reverse=True)
    all = 0
    for i in range(len(res)):
        all += res[i]
    return all


if __name__ == '__main__':
    # s = ""
    # print(findRepeatedDnaSequences(s))
    p = [70,4,83,56,94,72,78,43,2,86,65,100]
    k = 3
    print(maxProfit2(k, p))