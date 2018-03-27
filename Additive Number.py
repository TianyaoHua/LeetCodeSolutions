class Solution(object):
    def isValid(self, num, i, j, n):
        k = 0
        if j - i > 1 and num[i] == '0':
            return False
        if i - k > 1 and num[k] == '0':
            return False
        while j < n:
            add1 = int(num[k:i])
            add2 = int(num[i:j])
            sum_ = str(add1 + add2)
            if num[j:j+len(sum_)] == sum_:
                k = i
                i = j
                j = j + len(sum_)
            else:
                return False
        return True


    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n//2+n%2):
            for j in range(i+1, n//2+i+1):
                if self.isValid(num,i,j,n):
                    print(i, j)
                    return True

        return False

solution = Solution()
num = ("0235813")
print(solution.isAdditiveNumber(num))