class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        total_path = m + n -2
        sub_path = (n - 1) if m > n else (m - 1)
        factor, upper_factor = 1, 1
        for i in range(1, sub_path + 1):
            factor *= i
            upper_factor *= (total_path - i + 1)
        return upper_factor / factor

m = 1
n = 1
s = Solution()
print s.uniquePaths(m, n)