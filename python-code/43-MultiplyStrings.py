class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == 0:
            return "0"
        num2_len = len(num2)
        ans = ""
        for i in range(num2_len):
            idx = num2_len - i - 1
            cur = int(num2[idx])
            now_ans = self.multiplyOne(num1, cur, i)
            ans = self.addStr(ans, now_ans)
        return ans


    def addStr(self, ans, now_ans):
        if len(ans) < len(now_ans):
            # len(ans) >= len(now_ans)
            return self.addStr(now_ans, ans)
        ret = ""
        i, j = len(ans)-1, len(now_ans) - 1
        flag = 0
        while i >= 0 and j >= 0:
            cur = flag + int(ans[i]) + int(now_ans[j])
            ret = str(cur % 10) + ret
            flag = cur / 10
            i -= 1
            j -= 1
        while flag > 0 and i >= 0:
            cur = flag + int(ans[i])
            ret = str(cur % 10) + ret
            flag = cur/10
            i -= 1
        if flag == 0:
            ret = ans[:i+1] + ret
        else:
            ret = str(flag) + ret
        return ret


    def multiplyOne(self, num1, cur, idx):
        ans = ""
        for i in range(idx):
            ans += "0"
        flag = 0
        for i in range(len(num1)-1, -1, -1):
            int_num = int(num1[i])
            now_mul = flag + cur * int_num
            ans = str(now_mul % 10) + ans
            flag = now_mul / 10
        if flag > 0:
            ans = str(flag) + ans
        return ans


s = Solution()
num1 = "123"
num2 = "1000000"
print s.multiply(num1, num2)