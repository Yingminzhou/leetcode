class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.searchRange(nums, target, 0, len(nums)-1)

    def searchRange(self, nums, target, l, r):
        if l > r:
            return l
        mid = (l+r)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if mid > 0:
                if nums[mid-1] == target:
                    return mid - 1
                elif nums[mid-1] > target:
                    return self.searchRange(nums, target, l, mid-1)
                else:
                    return mid
            else:
                return mid
        else:
            return self.searchRange(nums, target, mid+1, r)

s = Solution()
nums = [1,3,5,6]
target = 0
print s.searchInsert(nums, target)