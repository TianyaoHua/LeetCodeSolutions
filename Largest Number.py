class Solution:
    # @param {integer[]} nums
    # @return {string}
    def digits(self, num):
        d = []
        if not num:
            return [[0], 1]
        while num > 0:
            d.append(num % 10)
            num = num // 10
        return [d[::-1],len(d)]

    def largestNumber(self, nums):
        dnums = []
        max_l = 0
        answer = ''
        for num in nums:
            [d, l_d] = self.digits(num)
            max_l = max(max_l, l_d)
            dnums.append([d, l_d])
        for i in range(len(dnums)):
            dnums[i][0] += ([dnums[i][0][j%dnums[i][1]] for j in range(2*max_l - dnums[i][1])])
        for i in range(2*max_l-1, -1, -1):
            dnums.sort(key=lambda x: x[0][i])
        for i in range(len(dnums)-1, -1, -1):
            for j in range(dnums[i][1]):
                answer += str(dnums[i][0][j])
        while len(answer) > 1 and answer[0] == '0':
            answer = answer[1:]
        return answer


solution = Solution()
nums = [830, 8308]
print(solution.largestNumber(nums))