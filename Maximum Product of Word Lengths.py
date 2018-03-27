class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lengths = [len(i) for i in words]
        sets=[set(i) for i in words]
        n = len(sets)
        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                if not sets[i].intersection(sets[j]):
                    answer = max(answer, lengths[i]*lengths[j])
        return answer

solution = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(solution.maxProduct(words))