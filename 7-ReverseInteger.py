import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        maxValue = math.pow(2, 31) - 1 
        minValue = - 1 * math.pow(2, 31)
        #print minValue, maxValue
        neg = False
        threshold1 = maxValue % 10
        threshold2 = maxValue / 10
        if x < 0:
            neg = True
            threshold1 = -1 * minValue % 10
            threshold2 = -1 * minValue / 10
            x = -1 * x
        while x != 0:
            flag = x % 10
            if ret > threshold2 or (ret == threshold2 and flag > threshold1):
                return 0
            ret = ret * 10 + flag
            x = x/10
        if neg:
            ret = -1 * ret
        return ret

s = Solution()
x = - math.pow(2, 31) 
print s.reverse(x)
