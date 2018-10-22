class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        if len(height) == 0:
            return ans
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    ans += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    ans += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return ans

height = [2,0,2]

s = Solution()
print s.trap(height)