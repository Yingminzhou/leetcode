import random

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        origin = list()
        # copy the list
        for i in range(len(nums)):
            origin.append(nums[i])
        self.quickSort(origin, 0, len(origin)-1)
        i = 0
        j = len(origin) - 1
        while i < j:
            nowSum = origin[i] + origin[j]
            if nowSum == target:
                break
            elif nowSum > target:
                j -= 1
            else:
                i += 1
        if i < j:
            start = -1
            end = -1
            isSet = False
            for k in range(len(nums)):
                if nums[k] == origin[i] and not isSet:
                    start = k
                    isSet = True
                elif nums[k] == origin[j]:
                    end = k
            if start > -1 and end > -1:
                if start > end:
                    return [end, start]
                else:
                    return [start, end]
    
    # quick sort
    def quickSort(self, origin, start, end):
        """
        :type origin: List[int]
        :type start: int
        :type start: end
        """
        if start > end:
            return
        self.randomList(origin, start, end)
        pivot = origin[start]
        i = start 
        j = end
        while i!=j:
            while origin[j] >= pivot and i<j :
                j -= 1
            while origin[i] <= pivot and i<j :
                i += 1
            if i < j:
                self.swap(origin, i, j)
        origin[start] = origin[i]
        origin[i] = pivot
        self.quickSort(origin, start, i-1)
        self.quickSort(origin, i+1, end)


    def swap(self, origin, a, b):
        if a >= len(origin) or b >= len(origin):
            return
        tmp = origin[a]
        origin[a] = origin[b]
        origin[b] = tmp

    def randomList(self, origin, start, end):
        tmp = random.randint(start, end)
        self.swap(origin, start, tmp)

nums = [2, 7, 11, 15, 8]
#nums = [3, 3]
target = 10
s = Solution()
print s.twoSum(nums, target)
#s.quickSort(nums, 0, len(nums)-1)
#print nums
