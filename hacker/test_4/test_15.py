def minDistance(word1: str, word2: str) -> int:
    if word1 == word2:
        return 0
    if word1 == None or word2 == None or len(word1) == 0 or len(word2) == 0:
        return max(len(word1), len(word2))
    if word1[0] == word2[0]:
        return minDistance(word1[1:], word2[1:])
    else:
        insert = minDistance(word1, word2[1:])
        delt = minDistance(word1[1:], word2)
        rep = minDistance(word1[1:], word2[1:])
        return 1 + min(insert, delt, rep)

def minDistance2(word1: str, word2: str) -> int:
    if len(word1) == 0 or len(word2) == 0:
        return max(len(word1), len(word2))
    distance = [[0 for x in range(len(word2))] for y in range(len(word1))]
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                if i - 1 >= 0 and j - 1>= 0:
                    distance_m = min(distance[i - 1][j - 1], distance[i - 1][j], distance[i][j - 1]) + 1
                    distance[i][j] = min(distance_m, distance[i - 1][j - 1])
                else:
                    distance[i][j] = max(i, j, 0)
            else:
                if i - 1 >= 0 and j - 1 >= 0:
                    distance[i][j] = min(distance[i - 1][j - 1], distance[i - 1][j], distance[i][j - 1]) + 1
                elif i == 0 and j == 0:
                    distance[i][j] = 1
                elif i == 0:
                    distance[i][j] = distance[i][j - 1] + 1
                elif j == 0:
                    distance[i][j] = distance[i - 1][j] + 1
    return distance[len(word1) - 1][len(word2) - 1]




if __name__ == '__main__':
    print(minDistance("ab", "bc"))
    print(minDistance2("ab", "bc"))