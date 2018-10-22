class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        ans = list()
        total_rnd = (n+1)/2
        if n > m:
            total_rnd = (m+1)/2
        for i in range(total_rnd):
            self.spiralKRound(matrix, i, m, n, ans)
        return ans


    def spiralKRound(self, matrix, k, m, n, ans):
        i = k
        j = k
        while j <= m-k-1:
            ans.append(matrix[i][j])
            j += 1
        j = m - k - 1
        if i == n - k - 1:
            return
        i = k + 1
        while i <= n-k-1:
            ans.append(matrix[i][j])
            i += 1
        i = n - k - 1
        if j == k:
            return
        j = m - k - 2
        while j >= k:
            ans.append(matrix[i][j])
            j -= 1
        j = k
        if i == k:
            return
        i = n - k - 2
        while i > k:
            ans.append(matrix[i][j])
            i -= 1

matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
s = Solution()
ans = s.spiralOrder(matrix)
print ans