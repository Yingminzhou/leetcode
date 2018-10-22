class Solution(object):
    r3, r9, poss_dict = range(3), range(9), {str(i) for i in range(1,10)}

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == ".":
                    for x in self.poss_dict - {row[k] for k in self.r9} - {board[k][j] for k in self.r9} \
                            - {board[i / 3 * 3 + m][j / 3 * 3 + n] for m in self.r3 for n in self.r3}:
                        board[i][j] = x
                        if self.solve(board):
                            return True
                        board[i][j] = "."
                    return False
        return True

s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

import time
start_ts = time.time()
s.solveSudoku(board)
end_ts = time.time()
print end_ts - start_ts
print board