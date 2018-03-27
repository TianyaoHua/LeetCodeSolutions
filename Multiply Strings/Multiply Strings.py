class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        dic_r = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        num1_int = 0
        n_1 = len(num1)
        for i in range(n_1):
            num1_int = num1_int*10 + dic.get(num1[i])
        s = 0
        n_2 = len(num2)
        for i in range(n_2):
            s = s * 10 + dic.get(num2[i]) * num1_int
        s_tr=''
        if not s:
            return '0'
        while s > 0:
            digit = s%10
            digit_str = dic_r.get(digit)
            s = (s-digit)/10
            s_tr = digit_str + s_tr
        return s_tr

if __name__ == "__main__":
    solution = Solution()
    answer = solution.multiply('0','123')
    print(answer)