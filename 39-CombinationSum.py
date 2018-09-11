class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        total_com = list()
        self.backtrack(total_com, list(), candidates, target, 0)
        return total_com



    def backtrack(self, total_com, tmp_list, candidates, remain, start):
        if remain < 0:
            return False
        elif remain == 0:
            total_com.append(tmp_list[:len(tmp_list)])
            return False
        else:
            for i in range(start, len(candidates)):
                tmp_list.append(candidates[i])
                flag = self.backtrack(total_com, tmp_list, candidates, remain - candidates[i], i)
                tmp_list.pop()
                #remain = remain + candidates[i]
                if not flag:
                    break
            return True



s = Solution()
candidates = [2,3,5]
target = 8
print s.combinationSum(candidates, target)