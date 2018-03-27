class Solution(object):
    def check(self, u, characters,k):
        for key in characters:
            if 0 < characters[key][u[1]+1]-characters[key][u[0]] < k:
                return False
        return True

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        characters = {c:[0] for c in s}
        for c in s:
            for key in characters:
                characters[key].append(characters[key][-1])
            characters[c][-1] += 1
        answer = 0
        n = len(s)
        for i in range(n):
            if characters[s[i]][i+1] >= k:
                j = 0
                while j <= i-k+1 and not self.check([j, i], characters, k):
                    j += 1
                if j <= i-k+1:
                    answer = max(answer, i-j+1)
        return answer





solution = Solution()
print(solution.longestSubstring('abcdedghijklmnopqrstuvwxyz',2))
