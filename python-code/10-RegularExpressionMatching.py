class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
        	return not s
        firstMatch = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
        	# repeat 0 time or repeat 1+ time
        	return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:
        	# continue to match
        	return firstMatch and self.isMatch(s[1:], p[1:])