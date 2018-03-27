class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        v = []
        p_ = set()
        s = [1 for i in range(n)]
        for i in range(1, n-1):
            if (ratings[i-1] < ratings[i] and ratings[i+1] <= ratings[i]) or (ratings[i-1] <= ratings[i] and ratings[i+1] < ratings[i]):
                p_.update({i})
            if (ratings[i-1] > ratings[i] and ratings[i+1] >= ratings[i]) or (ratings[i-1] >= ratings[i] and ratings[i+1] > ratings[i]):
                v.append(i)
        if ratings[1] > ratings[0]:
            v.insert(0, 0)
        elif ratings[1] < ratings[0]:
            p_.update({0})
        if ratings[n-1] < ratings[n-2]:
            v.append(n-1)
        elif ratings[n-1] > ratings[n-2]:
            p_.update({n-1})
        for vally in v:
            i = vally + 1
            if i < n and ratings[i] > ratings[vally]:
                while i not in p_:
                    s[i] = s[i-1] + 1
                    i += 1
                s[i] = s[i-1] + 1
        for vally in v:
            i = vally - 1
            if i >= 0 and ratings[i] > ratings[vally]:
                while i not in p_:
                    s[i] = s[i+1] + 1
                    i -= 1
                s[i] = max(s[i], s[i+1] + 1)
        print(s)

solution = Solution()
ratings = [3, 1]
print(solution.candy(ratings))