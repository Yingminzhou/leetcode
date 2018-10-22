class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numDict:
                j = numDict[complement]
                if i > j:
                    return [j, i]
                else:
                    return [i, j]
            numDict[nums[i]] = i

#nums = [2, 7, 11, 15, 8]
nums = [2, 5, 5, 11]
target = 10
#target = 19
s = Solution()
print s.twoSum(nums, target)
#s.quickSort(nums, 0, len(nums)-1)
#print nums
