# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if not n:
            return []
        intervals.sort(key = lambda x: x.end)    # maybe its x.end
        j = 0
        merged = [0]*n
        merged[0] =intervals[0]
        for i in range(1, n):
            flag = 1
            for k in range(0, j+1):
                if intervals[i].start <= merged[k].end:
                    merged_interval = Interval(min(intervals[i].start, merged[k].start), max(intervals[i].end, merged[k].end))
                    merged[k] = merged_interval
                    j = k
                    flag = 0
                    break
            if flag:
                merged[j+1]= intervals[i]
                j += 1
        return merged[0:j+1]

if __name__ == "__main__":
    starts = [1,2,8,15]
    ends = [3,6,10,18]
    intervals = []
    for i in range(len(starts)):
        interval = Interval(starts[i],ends[i])
        intervals.append(interval)
    solution = Solution()
    solution.merge(intervals)

