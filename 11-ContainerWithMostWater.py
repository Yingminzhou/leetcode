class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(height)):
        	ai = height[i]
        	for j in range(i, len(height)):
        		aj = height[j]
        		if aj < ai:
        			now = (j-i) * aj
        		else:
        			now = (j-i) * ai
        		if now > ret:
        			ret = now
        return ret