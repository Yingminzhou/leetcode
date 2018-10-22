class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        nums.sort()
        for i in range(len(nums)):
            ans = self.permute(nums[i], ans)
            print ans
        return ans

    def permute(self, num, pre_list):
        now_list = []
        tmp_dict = dict()
        for i in range(len(pre_list)):
            tmp_list = pre_list[i]
            for j in range(len(tmp_list)+1): 
                val_list = tmp_list[:j] + [num] + tmp_list[j:]
                if str(val_list) not in tmp_dict:
                    now_list.append(val_list)
                    tmp_dict[str(val_list)] = 1 
        return now_list


s = Solution()
nums = [1,2,2,3,3]
print s.permuteUnique(nums)
