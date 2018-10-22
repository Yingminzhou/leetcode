class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isDec(s, False, False, False, False, False)

    def isDec(self, s, is_start, is_dot, is_e, is_valid, is_blank):
        num_list = [str(i) for i in range(10)]
        for i in range(len(s)):
            if s[i] == ' ':
                if is_start:
                    is_blank = True
                continue
            else:
                if is_blank:
                    return False
                if s[i] in ["+", "-"]:
                    if is_start:
                        return False
                elif s[i] == '.':
                    if is_dot or is_e:
                        return False
                    is_dot = True
                elif s[i] == 'e':
                    if not is_valid or is_e:
                        return False
                    else:
                        return self.isDec(s[i+1:], False, False, True, False, is_blank)
                elif s[i] in num_list:
                    is_valid = True
                else:
                    return False
                is_start = True
        return is_valid

sl = Solution()
s = "01 "
print sl.isNumber(s)