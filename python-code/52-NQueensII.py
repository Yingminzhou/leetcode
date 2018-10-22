class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        cur_ans = ["." * n] * n
        self.backtrack(cur_ans, ans, n, 0)
        return len(ans)



    def backtrack(self, cur_ans, ans, n, row):
        if row == n:
            tmp = [data for data in cur_ans]
            ans.append(tmp)
            return
        for col in range(n):
            if self.valid(cur_ans, n, row, col):
                self.replace(cur_ans, row, col, 'Q')
                self.backtrack(cur_ans, ans, n, row+1)
                self.replace(cur_ans, row, col, '.')


    def valid(self, board, n, i, j):
        if i >= n or j >= n:
            return False
        # check row and column
        for tmp in range(n):
            if board[i][tmp] == 'Q' or board[tmp][j] == 'Q':
                return False
        # check hypotenuse
        tmp_row, tmp_col = i, j
        while tmp_row >= 0 and tmp_col >= 0:
            if board[tmp_row][tmp_col] == 'Q':
                return False
            tmp_col -= 1
            tmp_row -= 1
        tmp_row, tmp_col = i, j
        while tmp_row >= 0 and tmp_col < n:
            if board[tmp_row][tmp_col] == 'Q':
                return False
            tmp_col += 1
            tmp_row -= 1
        return True

    def replace(self, cur_ans, i, j, char):
        tmp = cur_ans[i]
        tmp = tmp[:j] + char + tmp[j+1:]
        cur_ans[i] = tmp


s = Solution()
n = 4
ans = s.solveNQueens(n)
print ans