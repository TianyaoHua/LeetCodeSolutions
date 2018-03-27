class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        answer = 0
        sign1 = True
        sign2 = True
        if divisor == 0:
            return 'MAX_INT'
        elif divisor < 0:
            divisor = - divisor
            sign2 = False
        if dividend < 0:
            dividend = - dividend
            sign1 = False
        i = 0
        answer = 0
        while dividend >= divisor:
            while divisor<<i <= dividend:
                i += 1
            dividend -= divisor<<(i-1)
            answer += 1<<(i-1)
            i = 0
        if sign1 ^ sign2:
            return -answer
        else:
            return answer

if __name__ == "__main__":
    solution = Solution()
    q = solution.divide(-40,3)
    print(q)