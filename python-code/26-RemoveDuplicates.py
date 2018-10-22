class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return len(nums)
        first = 0
        end = first + 1
        while end < len(nums):
            if nums[first] == nums[end]:
                end += 1
            else:
                nums[first+1], nums[end] = nums[end], nums[first+1]
                first += 1
                end += 1
        return first + 1



s = Solution()
nums =  [0,0,1,1,1,2,2,3,3,4]
ret = s.removeDuplicates(nums)
for i in range(ret):
    print nums[i]