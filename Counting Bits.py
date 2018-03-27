class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        current_bits = 0
        current_number = 0
        current_top = 0
        i = 1
        answer = [0]
        while len(answer) < num+1:
            answer += [i+1 for i in answer]
        return answer[0: num+1]

solution = Solution()
print(solution.countBits(16))
