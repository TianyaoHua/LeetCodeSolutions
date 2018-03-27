class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        i = 0
        j = 1
        diff = A[i]-A[j]
        lengths = []
        while j < n:
            if A[j]-A[j-1] != diff:
                if j - i >= 3:
                    lengths.append(j-i)
                i = j-1
                diff = A[j]-A[j-1]
            j += 1
        if j - i >= 3:
            lengths.append(j-i)
        answer = 0
        for length in lengths:
            answer += ((length-1)*(length-2))>>1
        return answer

solution = Solution()
print(solution.numberOfArithmeticSlices([1,2,3,4]))


