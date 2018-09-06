class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        num = len(board[0])
        for i in range(num):
            row = self.getRow(board, i)
            isValid = self.checkList(row)
            if not isValid:
                return False
        for j in range(num):
            column = self.getColumn(board, j)
            isValid = self.checkList(column)
            if not isValid:
                return False
        for i in range(0, num, num/3):
            for j in range(0, num, num/3):
                sub = self.getSubCub(board, i, j)
                isValid = self.checkList(sub)
                if not isValid:
                    return False
        return True


    def getRow(self, board, idx):
        if idx < len(board):
            return board[idx]
        return None

    def getColumn(self, board, idx):
        retList = list()
        for dataList in board:
            if idx >= len(dataList):
                return None
            else:
                retList.append(dataList[idx])
        return retList

    def getSubCub(self, board, rIdx, cIdx):
        retList = list()
        if rIdx + 2 >= len(board):
            return None
        retList = board[rIdx][cIdx: cIdx+3]
        retList += board[rIdx+1][cIdx: cIdx+3]
        retList += board[rIdx+2][cIdx: cIdx+3]
        return retList


    def checkList(self, dataList):
        tmpDict = dict()
        if len(dataList) != 9:
            return False
        for data in dataList:
            if data != ".":
                if data in tmpDict:
                    return False
                else:
                    tmpDict[data] = 1
        return True


s = Solution()
board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print s.isValidSudoku(board)