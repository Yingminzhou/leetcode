class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        last, cur, step = 0, 0, 0
        for i in range(num_len):
            if i > last:
                last = cur
                step += 1
            now = nums[i] + i
            if now > cur:
                cur = now
        return step if cur >= num_len - 1 else 0

s = Solution()
nums = [2,3,1,1,4]
print s.jump(nums)