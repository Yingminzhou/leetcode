class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        cir_num = (n+1) / 2
        ans = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        for now_cir in range(cir_num):
            i, j = now_cir, now_cir
            while j <= n - 1 - now_cir:
                ans[i][j] = num
                num += 1
                j += 1
            i += 1
            j = n - 1 - now_cir
            while i <= n - 1 - now_cir:
                ans[i][j] = num
                num += 1
                i += 1
            j -= 1
            i = n - 1 - now_cir
            while j >= now_cir:
                ans[i][j] = num
                num += 1
                j -= 1
            i -= 1
            j = now_cir
            while i >= now_cir + 1:
                ans[i][j] = num
                num += 1
                i -= 1
        return ans


n = 4
s = Solution()
ans = s.generateMatrix(n)
print ans