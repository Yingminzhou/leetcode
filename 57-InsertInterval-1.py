# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        cur_start, cur_end = newInterval.start, newInterval.end
        for i in range(len(intervals)):
            now_ans = intervals[i]
            now_start, now_end = now_ans.start, now_ans.end
            if cur_end < now_start:
                intervals.insert(i, newInterval)
                return intervals
            if cur_start > now_end:
                continue
            if now_end >= cur_end:
                new_start = now_start if now_start < cur_start else cur_start
                intervals[i] = Interval(new_start, now_end)
                return intervals
            else:
                start_now = i
                while i < len(intervals) and now_start <= cur_end:
                    i += 1
                    if len(intervals) > i:
                        now_ans = intervals[i]
                        now_start = now_ans.start
                end_now = i
                new_start = intervals[start_now].start if intervals[start_now].start < cur_start else cur_start
                new_end = intervals[end_now-1].end if intervals[end_now-1].end > cur_end else cur_end
                del intervals[start_now: end_now]
                intervals.insert(start_now, Interval(new_start, new_end))
                return intervals
        intervals.append(newInterval)
        return intervals

a = Interval(2,6)
b = Interval(1,2)
c = Interval(8,10)
d = Interval(15,18)

intervals = []
s = Solution()
ans =  s.insert(intervals, a)
for tmp in ans:
    print tmp.start,tmp.end


