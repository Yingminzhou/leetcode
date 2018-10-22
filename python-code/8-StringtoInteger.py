import math

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # init the digit dict
        digitDict = {'1': 1, '0': 0, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6, '9': 9, '8': 8}
            
        # to denote the process is start or not
        isStart = False
        # to denote the number is positive or not
        isPositive = True
        isOverFlow = False
        maxInt = int(math.pow(2, 31)) - 1
        minInt = -1 * int(math.pow(2, 31))
        threahold1 = maxInt / 10
        threahold2 = maxInt % 10
        ret = 0
        for i in range(len(str)):
            w = str[i]
            if w == ' ':
                if isStart:
                    break
                else:
                    continue
            elif w == '+':
                if not isStart:
                    isStart = True
                    isPositive = True
                else:
                    break
            elif w == '-':
                if not isStart:
                    isStart = True
                    isPositive = False
                    threahold1 = -1 * minInt / 10
                    threahold2 = -1 * minInt % 10
                else:
                    break
            elif w in digitDict:
                n = digitDict[w]
                if not isStart:
                    isStart = True
                if  (ret > threahold1  or (ret == threahold1 and n > threahold2)):
                    isOverFlow = True
                    break
                ret = ret * 10 + n
            else:
                break
        if isPositive:
            if isOverFlow:
                return maxInt
            else:
                return ret
        else:
            if isOverFlow:
                return minInt
            else:
                return -1 * ret



s = Solution()
str = "4193 with words"
print s.myAtoi(str)