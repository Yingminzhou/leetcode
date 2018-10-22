class Solution(object):
    rightDict = {"}": "{", ")":"(", "]":"["}
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackList = ['#']
        for i in range(len(s)):
            c = s[i]
            if c in self.rightDict:
                left = self.rightDict[c]
                if stackList[-1] != left:
                    return False
                else:
                    stackList = stackList[:-1]
            else:
                stackList.append(c)
        if len(stackList) == 1:
            return True
        else:
            return False


sl = Solution()
s = ""
print sl.isValid(s)