class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l_h = len(haystack)
        l_n = len(needle)
        if l_h >= l_n > 0 :
            for i in range(l_h - l_n + 1):
                if haystack[i] == needle[0]:
                    if haystack[i:i+l_n] == needle:
                        return i
        elif l_n == 0:
            return 0
        return -1

if __name__=="__main__":
    solution = Solution()
    answer = solution.strStr('needle in a haystack','')
    print(answer)