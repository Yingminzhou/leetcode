class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        next_jump = [0]
        check_dict = dict()
        return self.jumpN(nums, next_jump, check_dict)




    def jumpN(self, nums, next_jump, check_dict):
        now_jump = list()
        for now_idx in next_jump:
            check_dict[now_idx] = 1
            cur_num = nums[now_idx]
            if cur_num + now_idx >= len(nums) - 1:
                return 1
            for i in range(1, cur_num+1):
                next = now_idx + i
                if next not in check_dict:
                    now_jump.append(next)
        if len(now_jump) == 0:
            return 0
        return 1 + self.jumpN(nums, now_jump, check_dict)


s = Solution()
nums = [0,1,2]
print s.jump(nums)