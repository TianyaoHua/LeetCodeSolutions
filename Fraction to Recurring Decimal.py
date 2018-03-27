class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1
        if numerator < 0:
            numerator = -numerator
            sign *= -1
        elif numerator == 0:
            return '0'
        if denominator < 0:
            denominator = -denominator
            sign *= -1
        q =[numerator // denominator]
        r =[numerator % denominator]
        R = r[-1]
        while R:
            new_numerator = R * 10
            q.append(new_numerator // denominator)
            R = new_numerator % denominator
            if R not in r:
                r.append(R)
            else:
                break
        answer = str(q[0]) + '.'
        if not R:
            l_q = len(q)
            if l_q > 1:
                for i in range(1, len(q)):
                    answer += str(q[i])
            else:
                answer = answer[0:-1]
        else:
            p = r.index(R)+1
            for i in range(1, p):
                answer += str(q[i])
            answer += '('
            for i in range(p, len(q)):
                answer += str(q[i])
            answer += ')'
        if sign == -1:
            answer = '-' + answer
        return answer

solution = Solution()
numerator = 0
denominator = 8
print(solution.fractionToDecimal(numerator,denominator))
