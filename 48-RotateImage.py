class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2):
        	self.rotateSub(matrix, i, i, n-1-i, n)


    def rotateSub(self, matrix, row, start_col, end_col, n):
    	for i in range(start_col, end_col):
    		now_pos = [row, i]
    		# after pos: i, n-1-row
    		after_pos = [i, n-1-row]
    		while now_pos != after_pos:
    			next_pos = [after_pos[1], n-1-after_pos[0]]
    			self.swap(matrix, now_pos, after_pos)
    			after_pos = next_pos
    			#print now_pos, after_pos

    def swap(self, matrix, now_pos, after_pos):
    	now_row, now_col = now_pos
    	after_row, after_col = after_pos
    	tmp = matrix[now_row][now_col]
    	matrix[now_row][now_col] =  matrix[after_row][after_col]
    	matrix[after_row][after_col] = tmp


matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s = Solution()
s.rotate(matrix)
print matrix