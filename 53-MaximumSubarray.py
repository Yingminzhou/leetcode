class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        max, pre = nums[0], nums[0]
        for i in range(1, len(nums)):
            now = nums[i]
            if pre > 0:
                now += pre
            if now > max:
                max  = now
            pre = now
        return max

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print s.maxSubArray(nums)