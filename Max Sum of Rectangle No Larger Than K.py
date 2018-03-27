import numpy as np
class Solution(object):
    def online(self, array, i, j, k):
        if i == j:
            if array[i] <= k:
                return array[i]
            else:
                return -float('inf')
        else:
            p = (i+j)//2
            left = [array[p]]
            right = [array[p+1]]
            for q in range(p+1,i-1,-1):
                left.append(left[-1]+array[q])
            for q in range(p+1,j+1):
                right.append(left[1]+array[q])
            right.sort()
            left.sort()
            s = -float('inf')
            q = len(right)-1
            l = len(left)-1
            while q > 0 and l > 0 and right[q]+left[l] > k:
                if right[q] > left[l]:
                    l -= 1
                else:
                    q -= 1
            if q == 0:
                while l >= 0 and right[q] + left[l] > k:
                    l -= 1
            if l == 0:
                while q >= 0 and right[q] + left[k] > k:
                    q -= 1
            if l >= 0 and q >= 0:
                return max(right[q]+left[l], self.online(array, i, p, k), self.online(array, p+1,j,k))
            else:
                return max(self.online(array,i,p,k), self.online(array, p+1, j, k))

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # n = len(matrix)
        # m = len(matrix[0])
        print(matrix)
        print(k)
        return self.online(matrix, 0, len(matrix)-1, k)


solution = Solution()
matrix = list(np.random.randint(-10,10,100))
k = np.random.randint(-5,5)
print(solution.maxSumSubmatrix(matrix,k))

