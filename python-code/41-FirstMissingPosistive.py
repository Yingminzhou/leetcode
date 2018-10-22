class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        tmp_list = [0 for _ in range(num_len+1)]
        for i in range(num_len):
            if 0 < nums[i] <= num_len:
                tmp_list[nums[i]] = 1
        for i in range(1, num_len+1):
            if tmp_list[i] == 0:
                return i
        return num_len + 1


nums = [3,4,-1,1]
s = Solution()
print s.firstMissingPositive(nums)