class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = list()
        answer = 0;
        # if x>0:
        #     flag = 1;
        # else:
        #     flag = 0;
        while(x != 0):
            residential = int(x/10)
            remainder = x - residential*10
            x = residential
            digits.append(remainder)
        # if flag:
        for i in digits:
            answer = answer*10 + i;
        # else:
        #     for i in digits:
        #         answer = answer*10 + i;
        #     answer = -answer
        return answer

if __name__=="__main__":
    solution = Solution();
    answer = solution.reverse(-123)
    print(answer)

