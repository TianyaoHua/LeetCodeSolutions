class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_l = 0
        accumulative_l = 0
        s_sum = 0
        dic = {'(':1, ')':-1}
        check_point = -1
        check_flag = 1
        for i in range(n):
            s_sum += dic.get(s[i])
            accumulative_l += 1
            check_flag = 0
            if s_sum < 0:
                max_l = (accumulative_l - 1 > max_l) * (accumulative_l - 1) + (accumulative_l - 1 <= max_l) * max_l
                accumulative_l = 0
                s_sum = 0
                check_point = i
                check_flag = 1
        # if accumulative_l - s_sum > max_l:
        #     max_l = accumulative_l - s_sum
        if s_sum == 0 and not check_flag and accumulative_l > max_l:
            max_l = accumulative_l
        if s_sum > 0:
            max_r = 0
            s_sum = 0
            accumulative_l = 0
            for i in range(n-1, check_point, -1):
                s_sum += dic.get(s[i])
                accumulative_l += 1
                if s_sum > 0:
                    max_r = (accumulative_l - 1 > max_r) * (accumulative_l - 1) + (accumulative_l - 1 <= max_r) * max_r
                    accumulative_l = 0
                    s_sum = 0
            if accumulative_l + s_sum > max_r:
                max_r = accumulative_l - s_sum
            max_l = (max_l < max_r) * max_r + (max_l >= max_r) * max_l
        return max_l


if __name__ == "__main__":
    solution = Solution()
    answer = solution.longestValidParentheses("((())))))()")
    print(answer)

