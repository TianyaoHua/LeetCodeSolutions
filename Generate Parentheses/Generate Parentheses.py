class S(object):
    def __init__(self, string, s_sum, n_number):
        self.x =string
        self.sum = s_sum
        self.number = n_number

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        temp = []
        s = S('(', 1, 1)
        temp.append(s)
        for i in range(2*n-1):
            length = len(temp)
            for j in range(length):
                if  temp[j].number < n:
                    if temp[j].sum > 0:
                        string_derive = S('',0,0)
                        string_derive.x = temp[j].x
                        string_derive.number = temp[j].number
                        string_derive.sum = temp[j].sum
                        temp[j].x += '('
                        temp[j].number += 1
                        temp[j].sum += 1
                        inspector = temp[j].x
                        string_derive.x += ')'
                        string_derive.sum -= 1
                        inspector = string_derive.x
                        temp.append(string_derive)
                    else:
                        temp[j].x += '('
                        inspector = temp[j].x
                        temp[j].number += 1
                        temp[j].sum += 1
                    continue
                if temp[j].number == n:
                    temp[j].x += ')'
                    temp[j].sum -= 1
                    inspector = temp[j].x
        for string in temp:
            answer.append(string.x)
        return answer

if __name__ == "__main__":
    solution = Solution()
    key = solution.generateParenthesis(3)
    print(key)

