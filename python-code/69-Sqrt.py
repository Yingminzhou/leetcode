class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        num = i * i
        while num <= x:
        	i += 1
        	num = i * i
        return i - 1