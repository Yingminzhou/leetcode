class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        height_len = len(height)
        if height_len == 0:
            return ans
        nums = [0 for _ in range(height_len)]
        max_right = 0
        for i in range(height_len-1, -1, -1):
            max_right = max_right if max_right > height[i] else height[i]
            nums[i] = max_right
        max_left = 0
        for i in range(0, len(height)):
            now_num = height[i]
            if now_num > max_left:
                max_left = now_num
            max_right = nums[i]
            ans += (max_left if max_left < max_right else max_right) - now_num
        return ans


height = [0,1,0,2,1,0,1,3,2,1,2,1]

s = Solution()
print s.trap(height)
