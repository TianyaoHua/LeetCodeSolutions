class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num_str = len(strs)
        if num_str != 0:
            end_pointer = 0
            min_length = len(strs[0])
            for i in range(num_str):
                current_str_l = len(strs[i])
                min_length = (current_str_l<min_length)*current_str_l + (current_str_l>=min_length)*min_length
            equal_flag = 1
            while equal_flag == 1 and end_pointer < min_length:
                i = 0
                while i < num_str-1 and strs[i][end_pointer] == strs[i+1][end_pointer]:
                    i += 1
                equal_flag = (i==num_str-1)
                end_pointer = end_pointer + 1*equal_flag
            answer = strs[0][0:end_pointer]
        else:
            answer = ""
        return answer

if __name__ == "__main__":
    solution = Solution()
    answer = solution.longestCommonPrefix([])
    print(answer)






