from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0, int(sqrt(c)+1)):
            root = sqrt(c-i*i)
            if root == int(root):
                return True
            return False