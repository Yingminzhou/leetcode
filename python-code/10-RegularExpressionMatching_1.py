class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
       	m = len(s)
       	n = len(p)
       	d = [[False] * (n+1) for i in range(m+1)]
       	d[-1][-1]= True
       	for i in range(m, -1, -1):
       		for j in range(n-1, -1, -1):
       			firstMatch = i < m and p[j] in {s[i], '.'}
       			if j+1 < n and p[j+1] == '*':
       				d[i][j] = d[i][j+2] or (firstMatch and d[i+1][j])
       			else:
       				d[i][j] = firstMatch and d[i+1][j+1]
       	return d[0][0]

so = Solution()
s = 'aa'
p = 'a*'
print so.isMatch(s, p)
