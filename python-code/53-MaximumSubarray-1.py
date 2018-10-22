class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        mid = len(nums)/2
        left = nums[:mid]
        max_l = self.maxSubArray(left)
        l_mid = left[-1]
        l_mid_max = l_mid
        for i in range(len(left)-2, -1, -1):
            l_mid += left[i]
            if l_mid > l_mid_max:
                l_mid_max = l_mid

        right = nums[mid:]
        max_r = self.maxSubArray(right)
        r_mid = right[0]
        r_mid_max = r_mid
        for i in range(1, len(right)):
            r_mid += right[i]
            if r_mid > r_mid_max:
                r_mid_max = r_mid

        if max_l >= max_r and max_l >= l_mid_max + r_mid_max:
            return max_l
        if max_r >= max_l and max_r >= l_mid_max + r_mid_max:
            return max_r
        return l_mid_max + r_mid_max


nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print s.maxSubArray(nums)