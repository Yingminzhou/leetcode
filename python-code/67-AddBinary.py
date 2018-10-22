class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
        	return self.addBinary(b, a)
        ans = ""
        idx = 0
        flag = 0
        while idx < len(b) or flag > 0:
            if idx < len(a):
                flag += int(a[len(a) - idx - 1])
            else:
            	break
            if idx < len(b):
                flag += int(b[len(b) - idx - 1])
            ans = str(flag%2) + ans
            flag = flag / 2
            idx += 1
        if flag == 0:
            ans = a[:len(a) - idx] + ans
        else:
            ans = str(flag) + ans
        return ans

a = "11"
b = "1111111"
s = Solution()
print s.addBinary(a, b) 