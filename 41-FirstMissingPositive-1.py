class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        for i in range(nums_len):
            while 0 < nums[i] <= nums_len and nums[nums[i]-1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(0, nums_len):
            if i+1 != nums[i]:
                return i + 1
        return nums_len + 1

nums = [3,4,-1,1]
s = Solution()
print s.firstMissingPositive(nums)