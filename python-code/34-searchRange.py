class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                lIdx = self.searchLRRange(nums, target, l, mid, True)
                rIdx = self.searchLRRange(nums, target, mid, r, False)
                return [lIdx, rIdx]
        return [-1, -1]


    def searchLRRange(self, nums, target, l, r, isLeft=True):
        mid = (l+r)/2
        if r < l:
            return -1
        tmp = r
        if isLeft:
            tmp = l
        if mid == tmp:
            if nums[mid] == target:
                return mid
        if nums[mid] > target:
            return self.searchLRRange(nums, target, l, mid-1, isLeft)
        elif nums[mid] < target:
            return self.searchLRRange(nums, target, mid+1, r, isLeft)
        else:
            if isLeft:
                tmpIdx = self.searchLRRange(nums, target, l, mid-1, isLeft)
            else:
                tmpIdx = self.searchLRRange(nums, target, mid+1, r, isLeft)
            if tmpIdx == -1:
                return mid
            else:
                return tmpIdx

s = Solution()
nums = [1,2,3,3,3,3,4,5,9]
target = 3
print s.searchRange(nums, target)


