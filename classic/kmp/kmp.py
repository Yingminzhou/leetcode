def getNextNew(p):
    pLen = len(p)
    next = [ 0 for _ in range(pLen)]
    k = -1
    j = 0
    next[0] = -1
    while j < pLen:
        if k == -1 or p[k] == p[j]:
            k += 1
            j += 1
            if p[k] == p[j]:
                next[j] = next[k]
            else:
                next[j] = k
        else:
            k = next[k]
    return next


def getNext(p):
    pLen = len(p)
    next = [ 0 for _ in range(pLen)]
    k = -1
    j = 0
    next[0] = k
    while j < pLen:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[j]
    return next

def kmp(s,p):
    next = getNext(p)
    sLen = len(s)
    pLen = len(p)
    k = -1
    i = 0
    j = 0
    while i < sLen and j < pLen:
        if k == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == pLen:
        return i - j
    else:
        return -1

    
