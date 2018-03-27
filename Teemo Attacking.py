class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        n = len(timeSeries)
        answer = 0
        i = 0
        j = 0
        while j < n-1:
            if timeSeries[j+1] - timeSeries[j] < duration:
                j += 1
            else:
                answer += (timeSeries[j]-timeSeries[i]+duration)
                j += 1
                i = j
        answer += (timeSeries[j]-timeSeries[i]+duration)
        return answer


print(Solution().findPoisonedDuration([1,3,8,9,14],2))

