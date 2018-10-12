class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(n/2+1):
        	one_num = n - i * 2
        	total_num = i + one_num
        	ans += self.calPro(total_num, i)
        return ans
    
    def calPro(self, n, digit):
    	if n - digit < digit:
    		digit = n - digit
    	upper_sum, bottom_sum = 1, 1
    	for i in range(1, digit + 1):
    		upper_num = n - i + 1
    		upper_sum *= upper_num
    		bottom_sum *= i
    	return upper_sum / bottom_sum