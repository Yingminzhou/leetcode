class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx = 0
        p_idx = 0
        match = 0
        start_idx = -1
        p = self.removeConMark(p)
        while s_idx < len(s):
            if p_idx < len(p) and (p[p_idx] == '?' or p[p_idx] == s[s_idx] ):
                s_idx += 1
                p_idx += 1
            elif p_idx < len(p) and p[p_idx] == '*':
                start_idx = p_idx
                match = s_idx
                p_idx += 1
            elif start_idx != -1:
                p_idx = start_idx + 1
                match += 1
                s_idx = match
            else:
                return False
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
        return p_idx == len(p)


    def removeConMark(self, p):
        ans = ""
        for i in range(0, len(p)):
            if i >= 1 and p[i] == p[i-1] == "*":
                continue
            else:
                ans += p[i]
        return ans



sl = Solution()
s = "mississippi"
p = "m??*ss*?i*pi"
print sl.isMatch(s, p)
#print sl.removeConMark(p)
