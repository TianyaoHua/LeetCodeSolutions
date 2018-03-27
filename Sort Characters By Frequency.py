class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        for c in s:
            if c not in dict:
                dict.update({c:0})
            dict[c] += 1
        array = []
        for c in dict:
            array.append([c, dict[c]])
        array.sort(key=lambda x:x[1], reverse=1)
        answer = ''
        for a in array:
            answer += a[0]*a[1]
        return answer


print(Solution().frequencySort('tree'))