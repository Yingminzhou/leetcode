class Solution(object):
    digitMap = {"2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        letterList = [""]
        for i in range(len(digits)):
            digit = digits[i]
            letterList = self.aLetterCombination(digit, letterList)
        return letterList


    def aLetterCombination(self, digit, letterList):
        if digit in self.digitMap:
            retList = []
            nowLetterList = self.digitMap[digit]
            for i in range(len(nowLetterList)):
                for j in range(len(letterList)):
                    retList.append( letterList[j]+nowLetterList[i])
            return retList
        else:
            return letterList

s = Solution()
digits = "23"
print s.letterCombinations(digits)