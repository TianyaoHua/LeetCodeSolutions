class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split('+')
        b = b.split('+')
        ax = int(a[0])
        ay = int(a[1][:-1])
        bx = int(b[0])
        by = int(b[1][:-1])
        a = ax*bx - ay*by
        b = ax*by + ay*bx
        return str(a) + "+" + str(b) + "i"

print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))
