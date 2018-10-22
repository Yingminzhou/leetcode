class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret_list = [[]]
        for i in range(len(nums)):
            ret_list = self.permuteList(nums[i], ret_list)
        return ret_list


    def permuteList(self, num, now_list):
        ret_list = list()
        for i in range(len(now_list)):
            n_list = now_list[i]
            for j in range(len(n_list)+1):
                tmp_list = n_list[:j] + [num] + n_list[j:]
                ret_list.append(tmp_list)
        return ret_list

nums = []
s = Solution()
print s.permute(nums)