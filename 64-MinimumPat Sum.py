class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i >= 1 and j >=1:
                    grid[i][j] = grid[i][j] + (grid[i-1][j] if grid[i-1][j] < grid[i][j-1] else grid[i][j-1])
                elif i >= 1:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif j >= 1:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
        return grid[m-1][n-1]

grid = [[0]]

s = Solution()
print s.minPathSum(grid)