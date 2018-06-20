class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        i = len(s) - 1
        length = i+1
        while i > -1:
            j = length-1
            while j > i:
                if s[i] < s[j]:
                    k = j - 1
                    while k > i and s[i] > s[k]:
                        k -= 1
                    string = s[0:i] + s[j] + (s[i+1:k+1] + s[i] + s[k+1:j] + s[j+1:])[::-1]
                    return int(string)
                j -= 1
            i -= 1
        return -1

print(Solution().nextGreaterElement(1234))
