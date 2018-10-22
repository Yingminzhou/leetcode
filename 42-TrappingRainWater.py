class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(height)):
            max_left, max_right = 0, 0
            for j in range(i, -1, -1):
                max_left = height[j] if height[j] > max_left else max_left
            for j in range(i, len(height)):
                max_right = height[j] if height[j] > max_right else max_right
            ans += (max_left if max_left < max_right else max_right) - height[i]
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print s.trap(height)