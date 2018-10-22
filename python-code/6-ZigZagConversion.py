class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s
        tGap = 2 * (numRows - 1)
        zigStr = ""
        for i in range(numRows):
            j = i
            loop = 0
            gap2 = i * 2
            gap1 = tGap - gap2
            while j < len(s):
                zigStr += s[j]
                if loop % 2 == 0:
                    j = j + gap1
                    if gap1 == 0:
                        j = j + gap2
                else:
                    j = j + gap2
                    if gap2 == 0:
                        j = j + gap1
                loop += 1
        return zigStr


s = Solution()
str = "A"
numRows = 1
print s.convert(str, numRows) 
