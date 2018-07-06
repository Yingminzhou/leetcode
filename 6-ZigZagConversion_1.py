class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        m = len(s)
        if m < numRows:
            m = numRows
        rows = []
        for i in range(m):
            rows.append('')
        goingDown = False
        curRow = 0
        for i in range(len(s)):
            rows[curRow] = rows[curRow] + s[i]
            if curRow == 0 or curRow == numRows -1:
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow -= 1
        ret = ""
        for i in range(len(rows)):
            ret += rows[i]
        return ret
