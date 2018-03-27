# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        n = len(intervals)
        index = {intervals[i]:i for i in range(n)}
        h = sorted(intervals, key=lambda x:x.start)
        t = sorted(intervals, key=lambda x:x.end)
        answer = [-1 for i in range(n)]
        i = 0
        j = 0
        while j < n:
            while j < n and h[j].start < t[i].end:
                j += 1
            if j < n:
                answer[index[t[i]]] = index[h[j]]
                i += 1
        return answer

interval_a =  [  ]

intervals = []
for interval in interval_a:
    intervals.append(Interval(interval[0], interval[1]))
solution = Solution()
print(solution.findRightInterval(intervals))