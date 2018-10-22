class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
        	return 0
        if n < 0:
        	return self.myPow(1.0/x, -n)
        ans = 1.0
        while n != 0:
        	if n % 2 != 0:
        		ans *= x
        	x *= x
        	n = n / 2
        return ans


x = 2
n = 10
s = Solution()
print s.myPow(x, n)