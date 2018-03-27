class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        answer = ''
        for i in range(32):
            t = 2**(i+1)
            n_t_m = m // t
            i_t_m = m % t
            n_t_n = n // t
            i_t_n = n % t
            if n_t_m == n_t_n and (i_t_n > t/2-1 and i_t_m > t/2-1):
                answer = '1'+answer
            else:
                answer = '0' + answer
        return int(answer, 2)




solution = Solution()
m = 0
n = 2147483647
print(solution.rangeBitwiseAnd(m, n))