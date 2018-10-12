class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
        	return False
        row_l, row_r = 0, len(matrix)-1
        while row_l <= row_r:
        	row_m = (row_l + row_r) / 2
        	if matrix[row_m][-1] == target:
        		return True
        	elif matrix[row_m][-1] < target:
        		row_l = row_m + 1
        	else:
        		if matrix[row_m][0] == target:
        			return True
        		elif matrix[row_m][0] > target:
        			row_r = row_m - 1
        		else:
        			return self.searchList(matrix[row_m], target)
        return False


    def searchList(self, data_list, target):
    	start, end = 0, len(data_list) - 1
    	while start <= end:
    		mid = (start + end) / 2
    		if data_list[mid] == target:
    			return True
    		elif data_list[mid] < target:
    			start = mid + 1
    		else:
    			end = mid - 1
    	return False


data_list = [[1, 3, 5, 6],[8, 9, 12, 16]]
target = 18
s = Solution()
print s.searchMatrix(data_list, target)