class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
        	return None
        closet = target - (nums[0] + nums[1] + nums[2])
        if closet == 0:
        	return target
        for i in range(len(nums)-2):
        	for j in range(i+1, len(nums)-1):
        		for k in range(j+1, len(nums)):
        			now = target - (nums[i] + nums[j] + nums[k])
        			if now == 0:
        				return target
        			if closet * closet > now * now:
        				closet = now
        return target - closet

s = Solution()
nums = [-1,2,1,-4]
target = 1
print s.threeSumClosest(nums, 1)