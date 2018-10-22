# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return list()
        ans = list()
        for j in range(len(intervals)):
            cur_int = intervals[j]
            ans = self.mergeSort(ans, cur_int)
        return ans

    def mergeSort(self, ans, cur_int):
        if len(ans) == 0:
            return [cur_int]
        cur_start, cur_end = cur_int.start, cur_int.end
        for i in range(len(ans)):
            now_ans = ans[i]
            now_start, now_end = now_ans.start, now_ans.end
            if cur_end < now_start:
                ans.insert(i, cur_int)
                return ans
            if cur_start > now_end:
                continue
            new_start = cur_start if cur_start <= now_start else now_start
            new_end = cur_end if cur_end >= now_end else now_end
            new_int = Interval(new_start, new_end)
            ans = ans[:i] + ans[i+1:]
            return self.mergeSort(ans, new_int)
        ans.append(cur_int)
        return ans

a = Interval(2,4)
b = Interval(1,2)
c = Interval(8,10)
d = Interval(15,18)

intervals = [a,b]
s = Solution()
ans =  s.merge(intervals)
for tmp in ans:
    print tmp.start,tmp.end