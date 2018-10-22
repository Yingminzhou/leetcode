class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = len(s) - 1
        j = len(p) - 1
        match = True
        while i>=0 and j >=0:
            sw = s[i]
            pw = p[j]
            if pw == '.':
                i -= 1
                j -= 1
            elif pw == '*':
                if j > 0:
                    ppw = p[j-1]
                    if ppw == '.':
                        i -= 1
                    elif ppw == sw:
                        i -= 1
                        j -= 2
                else:
                    i -= 1
            else:
                if sw == pw:
                    i -= 1
                    j -= 1
                else:
                    match = False
                    break
        if i != -1 or j != -1:
            match = False
        return match