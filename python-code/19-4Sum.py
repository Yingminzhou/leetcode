class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        # init dict
        numberDict = dict()
        for i in range(len(nums)):
            numberDict[nums[i]] = i
        tmpList = list()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    sum = nums[i] + nums[j] + nums[k]
                    targetNum = target - sum
                    if targetNum in numberDict:
                        idx = numberDict[targetNum]
                        if idx > k:
                            tmpList.append([nums[i], nums[j], nums[k], targetNum])
        print tmpList
        retList = self.filter(tmpList)
        return retList

    def filter(self, tmpList):
        resList =  list()
        if len(tmpList) == 0:
            return tmpList
        resList.append(tmpList[0])
        for i in range(1, len(tmpList)):
            tmpData = tmpList[i]
            tmpData.sort()
            isSame = False
            for j in range(len(resList)):
                resData = resList[j]
                resData.sort()
                if resData == tmpData:
                    isSame = True
                    break

            if not isSame:
               resList.append(tmpData)
        return resList




s = Solution()
nums = [2,-4,-5,-2,-3,-5,0,4,-2]
target = -14
print s.fourSum(nums, target)