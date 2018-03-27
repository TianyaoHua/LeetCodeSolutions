class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = 0
        tableT = dict()
        for c in t:
            if c not in tableT:
                target += 1
                tableT[c] = 0
            tableT[c] += 1
        start, end = 0, 0
        ln = len(s)
        minWindow = ln + 1
        result = None
        while end < ln:
            c = s[end]
            end += 1
            if c in tableT:
                tableT[c] -= 1
                if tableT[c] == 0:
                    target -= 1
                    if target == 0:
                        if minWindow > end - start:
                            minWindow = end - start
                            result = (start, end)
                        while start < end:
                            cc = s[start]
                            start += 1
                            if cc in tableT:
                                tableT[cc] += 1
                                if tableT[cc] == 1:
                                    if minWindow > end - start + 1:
                                        minWindow = end - start + 1
                                        result = (start-1, end)
                                    target += 1
                                    break
        if minWindow > ln:
            return ""
        else:
            return s[result[0]:result[1]]
if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.minWindow(s, t))