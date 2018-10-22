class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target, 0, len(nums)-1, False)

    def binarySearch(self, nums, target, l, r, isPivot):
        if r < l:
            return -1
        mid = (l+r)/2
        if nums[mid] == target:
            return mid
        else:
            if isPivot:
                if nums[mid] < target:
                    return self.binarySearch(nums, target, mid+1, r, isPivot)
                else:
                    return self.binarySearch(nums, target, l, mid-1, isPivot)
            else:
                isPivot = self.checkPivot(nums, mid)
                lIdx = self.binarySearch(nums, target, l, mid-1, isPivot)
                if lIdx >= 0:
                    return lIdx
                else:
                    rIdx = self.binarySearch(nums, target, mid+1, r, isPivot)
                    return rIdx

    def checkPivot(self, nums, mid):
        if mid == 0 or mid == len(nums)-1:
            return False
        if nums[mid-1] < nums[mid] < nums[mid+1]:
            return False
        else:
            return True


s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print s.search(nums, target)
