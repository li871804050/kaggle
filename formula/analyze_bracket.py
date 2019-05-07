import re
def bracket(s: str):
    left_bracket = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            left_bracket.append(i)
        elif s[i] == ')':
            if len(left_bracket) == 0:
                break
            pos = left_bracket.pop()
            formula_old = s[pos + 1: i]
            formula = getOneFormula(formula_old)
            if formula != formula_old:
                if (i + 1 < len(s)):
                    s = s[: pos] + formula + s[i + 1:]
                    i = pos + len(formula) - 1
                else:
                    s = formula
                    break
        i += 1
    return s.replace('IF', 'if')

def getOneFormula(s: str):
    if re.match('.*\*.*', s):
        return getProduct(s)
    if re.match('.*/.*', s):
        return getDiv(s)
    if re.match('.*\+.*', s):
        return getSum(s)
    if re.match('.*-.*', s):
        return getSub(s)

    if re.match('.*>=.*', s):
        return getGte(s)
    if re.match('.*>.*', s):
        return getGt(s)
    if re.match('.*<=.*', s):
        return getLte(s)
    if re.match('.*<.*', s):
        return getLt(s)
    if re.match('.*=.*', s):
        return getEq(s)

    if re.match('.*AND.*', s):
        return getAND(s)
    if re.match('.*OR.*', s):
        return getOR(s)
    if re.match('.*XOR.*', s):
        return getXOR(s)
    return s

def getProduct(s: str):
    s = s.replace(' ', '')
    words = s.split('*')
    res = 'product('
    for w in words:
        res += w + ','
    res = res[0: len(res) - 1] + ')'
    return res

def getSum(s: str):
    s = s.replace(' ', '')
    words = s.split('+')
    res = 'sum('
    for w in words:
        res += w + ','
    res = res[0: len(res) - 1] + ')'
    return res

def getDiv(s: str):
    s = s.replace(' ', '')
    words = s.split('/')
    return 'div(%s, %s)'%(words[0], words[1])

def getSub(s: str):
    s = s.replace(' ', '')
    words = s.split('-')
    return 'sub(%s, %s)'%(words[0], words[1])

def getGte(s: str):
    s = s.replace(' ', '')
    words = s.split('>=')
    return 'gte(%s, %s)' % (words[0], words[1])

def getGt(s: str):
    s = s.replace(' ', '')
    words = s.split('>')
    return 'gt(%s, %s)' % (words[0], words[1])

def getLte(s: str):
    s = s.replace(' ', '')
    words = s.split('<=')
    return 'lte(%s, %s)' % (words[0], words[1])

def getLt(s: str):
    s = s.replace(' ', '')
    words = s.split('<')
    return 'lt(%s, %s)' % (words[0], words[1])

def getEq(s: str):
    s = s.replace(' ', '')
    words = s.split('=')
    return 'eq(%s, %s)' % (words[0], words[1])

def getAND(s: str):
    s = s.replace(' ', '')
    words = s.split('AND')
    return 'and(%s, %s)' % (words[0], words[1])

def getOR(s: str):
    s = s.replace(' ', '')
    words = s.split('OR')
    return 'or(%s, %s)' % (words[0], words[1])

def getXOR(s: str):
    s = s.replace(' ', '')
    words = s.split('XOR')
    return 'xor(%s, %s)' % (words[0], words[1])

if __name__ == '__main__':
    # s = '(((45-new_days)/45)+1)'
    s = 'IF((IF(((((45-new_day)/45) + 1)>8), (6 + (10*(1/2))), (7 + ((9/3)*4))) > 5), IF((7<9), ((tt - 13)*7), 2), IF((1=3),8, (ob*6*(3 + 4))))'
    print(bracket(s))
    # s = '02+03'
    # s = re.match('.*\+.*', s)
    # print(s.endpos)