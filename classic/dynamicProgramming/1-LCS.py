# -*- coding: utf-8 -*-

# 使用动态规划法计算最长公共子序列
# 定义好状态以及状态的转移
# 使用一个矩阵a[m,n]记录截止前m个和前n个最长子序列的长度
# a[m,n] = 0 if m = 0 or n = 0
# a[m,n] = a[m-1, n-1] +1 if m > 1 and n > 1 and s1[m] = s1[n]
# a[m,n] = max(a[m-1, n] + a[m, n-1]) if m > 1 and n > 1 and s1[m] != s1[n]
def LongestCommonSubSequnce(s1, s2):
    """
    :type : str
    :type : str
    :rtype : int
    """
    # 初始化状态矩阵
    len1 = len(s1)
    len2 = len(s2)
    a = [ [ 0 for i in range(len1 + 1) ] for i in range(len2 + 1) ]
    for i in range(1, len2+1):
        w1 = s2[i-1]
        for j in range(1, len1+1):
            w2 = s1[j-1]
            if w1 == w2:
                a[i][j] = a[i-1][j-1] + 1
            else:
                a[i][j] = max(a[i-1][j], a[i][j-1])
            #print w1, w2, i, j ,a[i][j]
    #print a
    # 遍历得到最长子序列
    retStr = ""
    i = len2
    j = len1
    while i >= 1 and j >= 1:
        w1 = s2[i-1]
        w2 = s1[j-1]
        if w1 == w2:
            retStr = w1 + retStr
            i -= 1
            j -= 1
        else:
            # 优先从左边开始遍历
            if a[i-1][j] == a[i][j]:
                i -= 1
            else:
                j -= 1
    return retStr

if __name__ == '__main__':
    s1 = "BDCABA"
    s2 = "ABCBDAB"
    print LongestCommonSubSequnce(s1,s2)
