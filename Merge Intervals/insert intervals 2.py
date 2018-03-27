
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
        intervals = [Interval(-float('inf'),-float('inf'))]+intervals
        n = len(intervals)
        i = 0
        while i < n and intervals[i].start < newInterval.start:
            i += 1
        if intervals[i-1].end >= newInterval.start:
            i -= 1
        j = 0
        while j < n and intervals[j].start <= newInterval.end:
            j += 1
        j -= 1
        if j >= i:
            merged_interval = Interval(min(newInterval.start,intervals[i].start), max(newInterval.end,intervals[j].end))
            return intervals[1:i]+ [merged_interval]+intervals[j+1:]
        else:
            return intervals[1:j+1] + [newInterval] + intervals[i:]

if __name__ == "__main__":
    solution = Solution()
    intervals = [Interval(1,3),Interval(6,9)]
    newInterval = Interval(2,5)
    inserted = solution.insert(intervals,newInterval)
    for i in inserted:
        print(i.start,i.end)

