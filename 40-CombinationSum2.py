class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        total_com = list()
        total_dict = dict()
        self.backtrack(total_com, list(), candidates, target, 0, total_dict)
        return total_com


    def backtrack(self, total_com, tmp_list, candidates, remain, start, total_dict):
        if remain < 0:
            return False
        elif remain == 0:
            if str(tmp_list[:len(tmp_list)]) not in total_dict:
                total_com.append(tmp_list[:len(tmp_list)])
                total_dict[str(tmp_list[:len(tmp_list)])] = 1
            return False
        else:
            for i in range(start, len(candidates)):
                tmp_list.append(candidates[i])
                if i < len(candidates):
                    flag = self.backtrack(total_com, tmp_list, candidates, remain - candidates[i], i+1, total_dict)
                    tmp_list.pop()
                    if not flag:
                        break
            return True


s = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print s.combinationSum2(candidates, target)