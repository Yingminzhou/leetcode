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
            new_start = cur_start if cur_start <= now_start else now_start
            new_end = cur_end if cur_end >= now_end else now_end
            new_int = Interval(new_start, new_end)
            intervals = intervals[:i] + intervals[i + 1:]
            return self.insert(intervals, new_int)
        intervals.append(newInterval)
        return intervals
