class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        i = 0
        j = len(height) - 1
        while i < j:
            ai = height[i]
            aj = height[j]
            if ai > aj:
                area = (j-i) * aj
                j -= 1
            else:
                area = (j-i) * ai
                i += 1
            if area > ret:
                ret = area
        return ret
