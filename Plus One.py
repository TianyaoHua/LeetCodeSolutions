class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1
        i = n-1
        while carry and i > -1:
            s = digits[i] + carry
            if s >= 10:
                digits[i] = s-10
                i -= 1
            else:
                digits[i] = s
                carry = 0
        if carry :
            digits = [1] + digits
        return digits

if __name__ == "__main__":
    solution = Solution()
    answer = solution.plusOne([0])
    print(answer)