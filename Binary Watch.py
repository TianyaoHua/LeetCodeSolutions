import itertools
class Solution(object):
    def minutes(self, n, digits):
        answer_m = []
        if n > 5:
            return []
        else:
            ms = list(itertools.combinations([0, 1, 2, 3, 4, 5], n))
            for m in ms:
                minute = sum([digits[i] for i in m])
                if 10 <= minute <= 59:
                    answer_m.append(str(minute))
                elif minute<10:
                    answer_m.append('0'+str(minute))
        return answer_m

    def hours(self, n, digits):
        answer_h = []
        mh = list(itertools.combinations([0, 1, 2, 3], n))
        for h in mh:
            hour = sum([digits[i] for i in h])
            if hour < 12:
                answer_h.append(str(hour))
        return answer_h

    def combine(self, hours, minutes):
        answer = []
        for h in hours:
            for minute in minutes:
                answer.append(h + ':' + minute)
        return answer

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        answer = []
        digits = {0:1, 1:2, 2:4, 3:8, 4: 16, 5:32}
        for i in range(0,min(num+1,4)):
            hours = self.hours(i, digits)
            minutes = self.minutes(num-i, digits)
            answer += self.combine(hours, minutes)
        return answer

solution = Solution()
print(solution.readBinaryWatch(2))