class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            if nums[i] == 0:
                zero_idx = i
                j = zero_idx - 1
                while j >= 0:
                    if nums[j] > zero_idx - j:
                        break
                    j -= 1
                if j == -1:
                    return False
        return True

nums = [0]
s = Solution()
print s.canJump(nums)