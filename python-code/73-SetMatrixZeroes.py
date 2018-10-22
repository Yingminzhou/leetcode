class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
        	return
        m, n = len(matrix), len(matrix[0])
        col_list = [0 for _ in range(m)]
        row_list = [0 for _ in range(n)]
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			col_list[i] = 1
        			row_list[j] = 1
        for i in range(m):
        	if col_list[i] == 1:
        		self.setColRowZeros(matrix, i, m, n)
        for i in range(n):
        	if row_list[i] == 1:
        		self.setColRowZeros(matrix, i, m, n, False)

    def setColRowZeros(self, matrix, idx, m, n, is_col=True):
    	if is_col:
    		for i in range(n):
    			matrix[idx][i] = 0
    	else:
    		for i in range(m):
    			matrix[i][idx] = 0