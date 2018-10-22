class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nLen = len(nums)
        idx = nLen - 1
        while idx > 0:
        	pivot = nums[idx-1]
        	k = self.findK(nums, idx-1, nLen-1, pivot)
        	if k != -1:
        		nums[idx-1], nums[k] = nums[k], nums[idx-1]
        		break
        	else:
        		idx -= 1
        	self.quickSort(nums, idx, nLen-1)



    def findK(self, nums, start, end, pivot):
    	if nums[-1] <= pivot:
    		return -1
    	if nums[start] > pivot:
    		return start
    	mid = (start + end) / 2
    	if nums[mid] <= pivot:
    		return self.findK(nums, mid+1, end, pivot)
    	else:
    		return self.findK(nums, start, mid, pivot)



    def quickSort(self, nums, start, end):
        if start > end:
            return
        i = start
        j = end
        pivot = nums[start]
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[start],nums[i] = nums[i], nums[start]
        self.quickSort(nums, start, i-1)
        self.quickSort(nums, i + 1, end)


nums = [3,2,1,8,5]
s = Solution()
s.nextPermutation(nums)
print nums
