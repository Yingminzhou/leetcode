# -*- coding: utf-8 -*-

# 使用动态规划法计算最长公共子串
# 定义好状态以及状态的转移
# 使用一个矩阵a[m,n]记录截止前m个和前n个最长串的长度
# a[m,n] = 0 if m = 0 or n = 0
# a[m,n] = a[m-1, n-1] +1 if m > 1 and n > 1 and s1[m] = s1[n]
# a[m,n] = a[m-1, n-1] if m > 1 and n > 1 and s1[m] != s1[n]
# 发现计算每列的计算只与上一列有关，因此可以把矩阵优化为存储数组
def LongestCommonSubStr(s1, s2):
    """
    :type : str
    :type : str
    :rtype : int
    """
    # 初始化状态矩阵
    len1 = len(s1)
    len2 = len(s2)
    a = [ 0 for i in range(len1 + 1) ]
    maxLen = 0
    maxIdx1 = -1
    maxIdx2 = -1
    for i in range(1, len2+1):
        w1 = s2[i-1]
        b = [ val for val in a]
        a = [ 0 for k in range(len1 + 1) ]
        for j in range(1, len1+1):
            w2 = s1[j-1]
            if w1 == w2:
                a[j] = b[j-1] + 1
            else:
                a[j] = 0
                #a[j] = max(a[j-1],b[j])
            if a[j] > maxLen:
                maxLen = a[j]
                maxIdx1 = j-1
        #print w1, a
    startIdx = maxIdx1 + 1 - maxLen
    retStr = ""
    #print startIdx, maxIdx1, maxLen
    if startIdx >= 0 and startIdx <= len1 and maxIdx1 < len1 and maxIdx1 >=0:
        retStr = s1[startIdx: maxIdx1 + 1]
        #print retStr
    #print a
    #print a
    return retStr

if __name__ == '__main__':
    s2 = "abacdfgdcab"
    s1 = "abacdgfdcabac"
    print LongestCommonSubStr(s1,s2)
