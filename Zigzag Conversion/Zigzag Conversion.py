class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        answer = list()
        if not 1 == numRows:
            for i in range(0,length,2*numRows-2):
                answer.append(s[i])
            for i in range(1,numRows-1):
                for j in range(0,length+2*numRows-2,2*numRows-2):
                    if i+j<length:
                        answer.append(s[i+j])
                    if 2*numRows-2-i+j<length:
                        answer.append(s[2*numRows-2-i+j])
            for i in range(numRows-1,length,2*numRows-2):
                answer.append(s[i])
            answer = "".join(answer)
        else:
            answer = s
        return answer

if __name__=="__main__":
    solution = Solution()
    answer = solution.convert("123456",3);
    print(answer)
