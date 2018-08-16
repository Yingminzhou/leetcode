class Solution(object):
    
    symbolDict = {"M": 1000, "CM": 900, "D": 500, "CD":400, "C":100, "XC": 90, "L":50, "XL": 40, "X": 10, "IX":9, "V": 5, "IV": 4, "I": 1}
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = 0
        res = 0
        while idx < len(s):
        	symbol = s[idx]
        	if idx < len(s) - 1:
        		if s[idx:idx+2] in self.symbolDict:
        			symbol = s[idx: idx+2]
        			idx += 1
        	res += self.symbolDict[symbol]
        	idx += 1
        return res