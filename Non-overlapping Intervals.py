# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x:x.e)
        answer = 0
        last_interval = intervals[0]
        n = len(intervals)
        for i in range(1, n):
            if intervals[i].s >= last_interval.e:
                answer += 1
            else:
                last_interval = intervals[i]
        return answer

