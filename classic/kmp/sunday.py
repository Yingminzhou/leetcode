def getNext(p):
    nextDict = dict()
    pLen = len(p)
    for i in range(pLen):
        nextDict[p[i]] = pLen - i
    return nextDict

def sunday(s,p):
    nextDict = getNext(p)
    sLen = len(s)
    pLen = len(p)
    i = 0
    j = 0
    while i < sLen:
        endIdx = i + pLen
        while j < pLen and i < sLen and s[i] == p[j]:
            i += 1
            j += 1
        if j < pLen and endIdx < sLen:
            endVal = s[endIdx]
            if endVal in nextDict:
                #moving nextDict[endVal]
                i = endIdx - pLen + nextDict[endVal]
            else:
                i = endIdx + 1
            j = 0
        else:
            break
    if j == pLen:
        return i - j
    else:
        return -1


s = "substring searaching algorithm"
p = "search"

print sunday(s,p)

