class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
        	return
        m, n = len(matrix), len(matrix[0])
        col_zero = False
        for i in range(n):
            if matrix[0][i] == 0:
                col_zero = True
        row_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                row_zero = True
        for i in range(1, m):
        	for j in range(1, n):
        		if matrix[i][j] == 0:
        			matrix[i][0] = 0
        			matrix[0][j] = 0
        for i in range(1, m):
        	if matrix[i][0] == 1:
        		self.setColRowZeros(matrix, i, m, n)
        for i in range(1, n):
        	if matrix[0][i] == 1:
        		self.setColRowZeros(matrix, i, m, n, False)
        if col_zero:
            self.setColRowZeros(matrix, 0, m, n)
        if row_zero:
            self.setColRowZeros(matrix, 0, m, n, False)

    def setColRowZeros(self, matrix, idx, m, n, is_col=True):
    	if is_col:
    		for i in range(n):
    			matrix[idx][i] = 0
    	else:
    		for i in range(m):
    			matrix[i][idx] = 0