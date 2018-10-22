class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return self.plusOnePlace(digits, len(digits)-1)

    def plusOnePlace(self, digits, place):
        now_sum = digits[place] + 1
        digits[place] = now_sum % 10
        if now_sum / 10 == 1:
            if place == 0:
                digits.insert(0, 1)
                return digits
            else:
                return self.plusOnePlace(digits, place-1)
        else:
            return digits

digits = [2, 9,9]
s = Solution()
print s.plusOne(digits)