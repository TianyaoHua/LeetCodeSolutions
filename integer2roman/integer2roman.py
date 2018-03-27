class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        answer = ""
        switcher = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        unit = 0.1
        while unit < 1000:
            unit *= 10
            digits = int((num % (unit*10) - num % unit)/unit)
            if digits < 4:
                unit_str = switcher.get(unit)
                for i in range(digits):
                    answer = unit_str + answer
            if digits == 4:
                unit_str = switcher.get(unit)
                suffix = switcher.get(unit * 5)
                answer = unit_str + suffix + answer

            # if digits == 5:
            #     unit_str = switcher.get(5*unit)
            #     answer = unit_str + answer
            if 9 > digits >= 5:
                unit_str = switcher.get(unit)
                prefix = switcher.get(unit*5)
                #answer = suffix + answer
                for i in range(digits-5):
                    answer = unit_str + answer
                answer = prefix + answer
            if digits == 9:
                unit_str = switcher.get(unit)
                suffix = switcher.get(unit*10)
                answer = unit_str + suffix + answer
        return answer

if __name__ == "__main__":
    solution = Solution()
    answer = solution.intToRoman(143)
    print(answer)