class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        previous_seg = '1.'
        current_seg = ''
        for i in range(n-1):
            j = 1
            k = 0
            length = len(previous_seg)
            while j < length:
                if previous_seg[j] != previous_seg[j-1]:
                    current_seg += str(j-k) + previous_seg[j-1]
                    k = j
                j += 1
            previous_seg = current_seg+'.'
            current_seg = ''
        current_seg = previous_seg[0:-1]
        return current_seg


if __name__ == "__main__":
    solution = Solution()
    answer = solution.countAndSay(3)
    print(answer)

