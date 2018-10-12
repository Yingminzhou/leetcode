class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        ans = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
        	for j in range(m+1):
        		if i == 0:
        			ans[i][j] = j
        		elif j == 0:
        			ans[i][j] = i
        		else:
        			flag = 0 if word1[j-1] == word2[i-1] else 1
        			min_val = ans[i-1][j-1] + flag
        			if min_val > ans[i-1][j] + 1:
        				min_val = ans[i-1][j] + 1
        			if min_val > ans[i][j-1] + 1:
        				min_val = ans[i][j-1] + 1
        			ans[i][j] = min_val
        return ans[n][m]

word1 = "horse"
word2 = "ros"
s = Solution()
print s.minDistance(word1, word2)