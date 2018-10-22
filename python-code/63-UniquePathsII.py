class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        s = [[1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    s[i][j] = 0
                else:
                    if i >= 1 and j >= 1:
                        s[i][j] = s[i-1][j] + s[i][j-1]
                    elif i >= 1:
                        s[i][j] = s[i-1][j]
                    elif j >= 1:
                        s[i][j] = s[i][j-1]
        return s[m-1][n-1]

obstacleGrid = [[0,0]]
s = Solution()
print s.uniquePathsWithObstacles(obstacleGrid)