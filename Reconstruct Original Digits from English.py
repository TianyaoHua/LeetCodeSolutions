from scipy.linalg import solve
import numpy as np
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = ['zero','one','two','three','four','five','six','seven','eight','nine']
        map = {'e':0, 'f':1, 'g':2, 'h':3, 'i':4, 'n':5, 'o':6, 'r':7, 's':8, 't':9, 'u':10, 'v':11, 'w':12, 'x':13, 'z':14}
        b = np.array([0 for i in range(15)])
        for c in s:
            b[map[c]] += 1
        a = np.array([[0 for i in range(15)] for j in range(10)])
        for i in range(10):
            word = dict[i]
            for c in word:
                a[i][map[c]] += 1
        a = a.transpose()
        i = 0
        while i < len(b) and len(b) > 10:
            if b[i] == 0:
                b = np.delete(b, i)
                a = np.delete(a,i,0)
                i -= 1
            i += 1
        a = np.array(a[0:10])
        x = solve(a,b)
        print(x)

solution = Solution()
print(solution.originalDigits('fviefuro'))