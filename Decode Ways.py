class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        table = [0]*(1+n)
        table[0] = 1
        map_ = {}
        for i in range(1, 27):
            map_.update({str(i): i})
        if s[0] in map_:
            table[1] = 1
        for i in range(2, n+1):
            if s[i-1] in map_:
                if s[i-2] + s[i-1] in map_:
                    table[i] = table[i-1] + table[i-2]
                else:
                    table[i] = table[i-1]
            else:
                if s[i-2] + s[i-1] in map_:
                    table[i] = table[i-2]
        return table[-1]

if __name__ == "__main__":
    solution = Solution()
    s = '01'
    print(solution.numDecodings(s))
