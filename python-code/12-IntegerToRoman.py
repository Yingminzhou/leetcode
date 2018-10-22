class Solution(object):
    symbolList = [{1000: "M"}, {900:"CM"}, {500:"D"}, {400:"CD"},{100:"C"}, {90:"XC"}, {50:"L"}, {40:"XL"},{10:"X"}, {9:"IX"}, {5:"V"}, {4:"IV"}, {1:"I"}]

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanStr = ""
        for i in range(len(self.symbolList)):
        	base, symbol = self.symbolList[i].items()[0]
        	cnt = num / base
        	for j in range(cnt):
        		romanStr += symbol
        	num = num % base
        	if num == 0:
        		break
    	return romanStr