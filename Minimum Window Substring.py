class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        n = len(t)
        for i in range(n):
            if t[i] in dic:
                dic[t[i]] += 1
            else:
                dic.update({t[i]: 1})
        m = len(s)
        q = {}
        in_q = 0
        i = 0
        while i < m and in_q < n:
            if s[i] in dic and dic[s[i]] > 0:
                if s[i] not in q:
                    q.update({s[i]: [i]})
                else:
                    q[s[i]].append(i)
                in_q += 1
                dic[s[i]] -= 1
            i += 1
        if in_q < n:
            return ""
        min_ = min(q[i][0] for i in q)
        max_ = max(q[i][-1] for i in q)
        min_window = [min_, max_]
        min_length = max_ - min_
        for i in range(min_, m):
            if s[i] in dic and i not in q[s[i]]:
                q[s[i]].append(i)
                q[s[i]].sort()
                q[s[i]].remove(q[s[i]][0])
                min_ = min(q[i][0] for i in q)
                max_ = max(q[i][-1] for i in q)
                window_length = max_ - min_
                if window_length < min_length:
                    min_length = window_length
                    min_window = [min_, max_]
        return s[min_window[0]: min_window[1]+1]




if __name__ == "__main__":
    solution = Solution()
    s = "aa"
    t = "aa"
    print(solution.minWindow(s, t))



