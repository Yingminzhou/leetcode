class Solution(object):
    def solveSudoku(self, board):
        def dfs():
            for i, row in enumerate(board):
                for j, char in enumerate(row):
                    if char == '.':
                        for x in s9 - {row[k] for k in r9} - {board[k][j] for k in r9} - \
                                {board[i / 3 * 3 + m][j / 3 * 3 + n] for m in r3 for n in r3}:
                            board[i][j] = x
                            if dfs(): return True
                            board[i][j] = '.'
                        return False
            return True

        r3, r9, s9 = range(3), range(9), {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        dfs()

s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

import time
start_ts = time.time()
s.solveSudoku(board)
end_ts = time.time()
print end_ts - start_ts
print board