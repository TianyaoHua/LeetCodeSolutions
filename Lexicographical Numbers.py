class Solution(object):
    def next(self, k, n):
        if 10*k <= n:
            return 10*k
        k = k+1
        if k <= n:
            while k%10 == 0:
                k = k//10
        else:
            k = k//10+(k%10!=0)
            while k%10 == 0:
                k = k//10
        return k

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer = [1]
        for _ in range(1, n):
            answer.append(self.next(answer[-1], n))
        return answer

    def check(self, n):
        s = [str(i) for i in range(1,n+1)]
        s.sort()
        return [int(i) for i in s]

solution = Solution()
print(solution.check(18))
print(solution.lexicalOrder(18))
for i in range(1,49999):
    if (solution.lexicalOrder(i) != solution.check(i)):
        print(i)