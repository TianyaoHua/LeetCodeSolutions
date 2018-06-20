class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time = []
        for x in timePoints:
            time.append(int(x[0:2]) * 60 + int(x[3:]))
        time.sort()
        answer = float('inf')
        for i in range(1, len(time)):
            answer = min(answer, time[i] - time[i-1], 1440-(time[i] - time[i-1]))
        answer = min(answer, time[-1] - time[0], 1440-(time[-1] - time[0]))
        return answer

print(Solution().findMinDifference(["05:31","22:08","00:35"]))