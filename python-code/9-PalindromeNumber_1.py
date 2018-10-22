class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 ==0 and x !=0):
        	return False
        invertNum = 0
        while x > invertNum:
        	invertNum = invertNum * 10 + x % 10
        	x = x / 10
        return x == invertNum or x == invertNum / 10