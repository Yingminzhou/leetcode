class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0 :
        	return 0
        if n < 0:
        	return self.myPow(1.0/x, -n)
        if n == 0:
            return 1
        ans = self.myPow(x, n/2)
        if n % 2 == 0:
            return ans * ans
        else:
            return ans * ans * x


x = 0.44528
n = 0
s = Solution()
print s.myPow(x, n)