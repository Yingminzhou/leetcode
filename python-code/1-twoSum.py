class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numLen = len(nums)
        for i in range(numLen):
            for j in range(i+1, numLen):
                if nums[i] + nums[j] == target:
                    return [i,j]

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print s.twoSum(nums, target)
