class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        first = 0
        end = first + 1
        while end < len(nums):
            if nums[first] != val:
                first += 1
                end += 1
            else:
                if nums[end] != val:
                    nums[first], nums[end] = nums[end], nums[first]
                    first = first + 1
                    end = end + 1
                else:
                    end += 1
        if nums[end-1] != val:
            return first + 1
        else:
            return first


nums = [3,3]
val = 2
s = Solution()
ret = s.removeElement(nums, val)
for i in range(ret):
    print nums[i]