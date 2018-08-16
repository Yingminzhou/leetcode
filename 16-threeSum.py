class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retList = list()
        idxDict = dict()
        dupDict = dict()
        for i in range(len(nums)):
        	idxDict[nums[i]] = i
        for i in range(len(nums)):
        	for j in range(i+1, len(nums)):
        		target = 0 - (nums[i] + nums[j])
        		if target in idxDict:
        			targetIdx = idxDict[target]
        			if targetIdx > j :
        				if target in dupDict:
        					numSet = dupDict[target]
        					if nums[i] not in numSet and nums[j] not in numSet:
        						#print target, nums[i], nums[j], num
        						retList.append([nums[i], nums[j], nums[targetIdx]]) 
        						nowSet = set()
        						if nums[i] in dupDict:
        							nowSet = dupDict[nums[i]]
        						nowSet.add(target)
        						dupDict[nums[i]] = nowSet
        						nowSet = set()
        						if nums[j] in dupDict:
        							nowSet = dupDict[nums[j]]
        						nowSet.add(target)
        						dupDict[nums[j]] =  nowSet
        						nowSet = set()
        						if target in dupDict:
        							nowSet = dupDict[target]
        						nowSet.add(nums[i])
        						dupDict[target] = nowSet
        				else:
        					#print nums[i],nums[j], target
        					retList.append([nums[i], nums[j], nums[targetIdx]])
        					nowSet = set()
        					if nums[i] in dupDict:
        						nowSet = dupDict[nums[i]]
        					nowSet.add(target)
        					dupDict[nums[i]] = nowSet
        					nowSet = set()
        					if nums[j] in dupDict:
       							nowSet = dupDict[nums[j]]
       						nowSet.add(target)
       						dupDict[nums[j]] =  nowSet
       						nowSet = set()
       						if target in dupDict:
       							nowSet = dupDict[target]
       						nowSet.add(nums[i])
       						dupDict[target] = nowSet
       	return retList


s = Solution()
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print s.threeSum(nums)