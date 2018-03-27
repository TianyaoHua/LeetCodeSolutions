class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        sign = ""
        if num < 0:
            sign = "-"
            num = - num
        elif num == 0:
            return '0'
        answer = ''
        while num > 0:
            answer += str(num%7)
            num = num//7
        return sign + answer[::-1]

print(Solution().convertToBase7(0))