
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if not n:
            return []
        intervals.sort(key = lambda x: x[1])    # maybe its x.end
        j = 0
        merged = [0]*n
        merged[0] =intervals[0]
        for i in range(1, n):
            flag = 1
            for k in range(0, j+1):
                if intervals[i][0] <= merged[k][1]:
                    merged_interval = [min(intervals[i][0], merged[k][0]), max(intervals[i][1], merged[k][1])]
                    merged[k] = merged_interval
                    j = k
                    flag = 0
                    break
            if flag:
                merged[j] = intervals[i]
                j += 1
        return merged[0:j+1]

if __name__ == "__main__":
    intervals = [[3,3],[1,1],[0,2],[2,2],[1,2],[1,3],[1,1],[3,3],[2,3],[4,6]]
    solution = Solution()
    print(solution.merge(intervals))
