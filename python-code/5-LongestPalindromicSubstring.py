class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        if m <= 1:
            return s
        # init the matrix, the diagonal value is True while others is false
        maxLen = 0
        res = ""
        a = [[ False for i in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(m):
                if i >= j:
                    a[i][j] = True
        for i in range(m, -1, -1):
            for j in range(i, m):
                if s[i] == s[j] and (j-i <= 2 or a[i+1][j-1]):
                    a[i][j] = True
                    if j-i+1 >= maxLen:
                        maxLen = j-i+1
                        res = s[i:j+1]
        return res

if __name__ == "__main__":
    s = Solution()
    s1 = "abcda"
    print s.longestPalindrome(s1)
    
