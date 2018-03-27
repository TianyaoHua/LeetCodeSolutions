
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        if not n:
            return [newInterval]
        i = 0
        while i < n and intervals[i].start < newInterval.start:
            i += 1
        if intervals[i-1].end >= newInterval.start:
            i -= 1
        j = 0
        while j < n and intervals[j].start <= newInterval.end:
            j += 1
        j -= 1
        if j==i==-1:
            return [newInterval] + intervals
        elif j >= i:
            merged_interval = Interval(min(newInterval.start,intervals[i].start), max(newInterval.end,intervals[j].end))
            return intervals[0:i]+ [merged_interval]+intervals[j+1:]
        else:
            return intervals[0:j+1] + [newInterval] + intervals[i:]