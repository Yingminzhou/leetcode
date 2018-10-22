class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            val = nums[i]
            if val == target:
                return i
            elif val > target:
                return i - 1
        return len(nums)