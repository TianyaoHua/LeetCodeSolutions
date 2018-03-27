class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dict = {c:i for i,c in enumerate(words)}
        answer = []
        for word in words:
            n = len(word)
            candidate = word[::-1]
            if candidate in dict and candidate != word:
                answer.append([dict[word],dict[candidate]])
            for i in range(1, n+1):
                if candidate[i:] in dict and word+candidate[i:] == (word+candidate[i:])[::-1]:
                    answer.append([dict[word], dict[candidate[i:]]])
                if candidate[0:n-i] in dict and candidate[0:n-i]+word == (candidate[0:n-i]+word)[::-1]:
                    answer.append([dict[candidate[0:n-i]], dict[word]])
        return answer

solution = Solution()
words = ["aba", "a"]
print(solution.palindromePairs(words))