class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        switcher = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        current_digit = 0
        previous_digit = 0
        answer = 0
        for i in range(len(s)-1,-1,-1):
            current_digit = switcher.get(s[i])
            answer = answer + (current_digit>=previous_digit)*current_digit - (current_digit<previous_digit)*current_digit
            previous_digit = current_digit
        return answer
if __name__ == "__main__":
    solution = Solution()
    integer = solution.romanToInt('XI')
    print(integer)