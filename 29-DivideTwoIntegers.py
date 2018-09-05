import math

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        minVal = -1 * math.pow(2, 31)
        if dividend == minVal and divisor == -1:
            return int(math.pow(2, 31) - 1)
        flag = 1
        if divisor < 0 and divisor < 0:
            divisor = divisor * -1
            dividend = dividend * -1
        if divisor > 0 > dividend:
            flag = -1
            dividend = dividend * -1
        if divisor < 0 < dividend:
            flag = -1
            divisor = divisor * -1
        return flag * self.dividePos(dividend, divisor)

    def dividePos(self, dividend, divisor):
        if dividend < divisor:
            return 0
        ret = 1
        nowSum = divisor
        while nowSum + nowSum <= dividend:
            nowSum += nowSum
            ret += ret
        return ret + self.divide(dividend - nowSum, divisor)





s = Solution()
#print s.divide(-math.pow(2, 31), -1)
#print math.pow(2,31)-1
#print s.divide(2147483647,1)
print s.divide(10,-3)