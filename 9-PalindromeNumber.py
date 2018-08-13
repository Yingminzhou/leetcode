class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = self.getReverse(x)
        if res == x:
        	return True
        else:
        	return False


    def getReverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        MAX_INT = pow(2, 31)
        while x>0:
        	flag = x % 10
        	if ret > MAX_INT/10 or (ret == MAX_INT/10 and flag > MAX_INT%10):
        		return MAX_INT
        	ret = ret * 10 + flag
        	x = x/10
        return ret


s = Solution()
x = 1
print s.isPalindrome(x)
