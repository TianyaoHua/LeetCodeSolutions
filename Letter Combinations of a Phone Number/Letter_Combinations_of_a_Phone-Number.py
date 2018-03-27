class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit2str_map = {'1': [1,"*"],'2': [3,"abc"],'3': [3,"def"],'4': [3,"ghi"],'5': [3,"jkl"],'6': [3,"mno"],'7': [4,"pqrs"],'8': [3,"tuv"],'9': [4,"wxyz"],'0': [1," "]}
        answer = [""]
        if digits == "":
            return []
        else:
            for digit in digits:
                [str_l, string] = digit2str_map.get(digit)
                temp =[]
                for i in range(str_l):
                    temp1 = answer[0:]
                    for j in range(len(answer)):
                        temp1[j] = temp1[j]+string[i]
                    temp += temp1[0:]
                answer = temp[0:]
        return answer

if __name__ == "__main__":
    solution = Solution()
    answer = solution.letterCombinations('1')
    print(answer)



