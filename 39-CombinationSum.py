class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        total_com = list()
        self.backtrack(total_com, list(), candidates, target, 0)
        return total_com
        


    def backtrack(self, total_com, tmp_list, candidates, remain, start):
    	if remain < 0:
    		return False
    	if remain == 0:
    		total_com.append(tmp_list)
    		return False
    	for i in range(start, len(candidates)):
    		tmp_list.append(candidates[i])
    		#print  total_com, tmp_list, remain - candidates[i], i, candidates[i]
    		#flag = self.backtrack(total_com, tmp_list, candidates, remain - candidates[i], i)
    		flag = self.backtrack(total_com, tmp_list, candidates, remain - candidates[i], i)
    		tmp_list = tmp_list[:-1]
    		if not flag:
    			break
    	return True


s = Solution()

candidates = [2,3,6,7]
target = 8

print s.combinationSum(candidates, target)