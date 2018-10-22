class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        isLast = False
        ans = 0
        while i >= 0:
            if s[i] == " ":
                if not isLast:
                    i -= 1
                    continue
                else:
                    return ans
            else:
                ans += 1
                isLast = True
            i -= 1
        return ans

s = "          a d "
sl = Solution()
print sl.lengthOfLastWord(s)

