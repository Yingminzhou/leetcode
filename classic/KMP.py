def KmpSearch(s, p, next):
    i = 0
    j = 0
    sLen = len(s)
    pLen = len(p)
    while i < sLen and j < pLen:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == pLen:
        return i - j
    else:
        return -1

def GetNext(p):
    pLen = len(p)
    next = [0 for i in range(pLen)]
    next[0] = -1
    k = -1
    j = 0
    while j < pLen - 1:
        if k == -1 or p[j] == p[k]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]
    return next

s="dabc"
p="aba"
next = GetNext(p)
print KmpSearch(s, p, next)