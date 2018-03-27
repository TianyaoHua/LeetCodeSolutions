class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p = 0
        q = len(numbers)-1
        s = numbers[p] + numbers[q]
        while s != target:
            if s > target:
                q -= 1
            else:
                p += 1
            s = numbers[p] + numbers[q]
        return p+1, q+1


solution = Solution()
numbers = [2, 7 ,11, 15]
print(solution.twoSum(numbers, 9))