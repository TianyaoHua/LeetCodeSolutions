class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start = -1
        end = -1
        answer = 0
        iteration = -1
        length = len(str);
        if str=="":
            return 0
        for i in str:
            iteration += 1
            if ord(i)>= 48 and ord(i) <= 57:
                if start<0:
                    start = iteration
            elif start >= 0 and end < 0:
                end = iteration
                break
            if start < 0 and i != ' ' and i != '+' and i != '-':
                break
            if (i == '+' or i == '-') and iteration < length-1:
                if ord(str[iteration+1]) < 48 or ord(str[iteration+1])>57:
                    break
        if end<0 and 48 <= ord(str[-1]) <= 57:
            end = iteration+1
        if start >= 0 and end >start:
            answer = str[start:end]
            answer = int(answer)
        if start > 0 and str[start-1] == '-':
            answer = -answer
        return answer

if __name__ == "__main__":
    solution = Solution()
    answer = solution.myAtoi("+ 1")
    print(answer)

