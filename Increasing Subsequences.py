class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        sequences = set()
        table = [set() for i in range(n)]
        for i in range(n):
            sequence = set()
            for j in range(0,i):
                if nums[i] >= nums[j]:
                    sequence.add((nums[j], nums[i]))
                    for s in table[j]:
                        sequence.add(tuple(list(s)+[nums[i]]))
            table[i] = sequence.copy()
            sequences.update(sequence)
        answer = [list(s) for s in sequences]
        return answer

print(Solution().findSubsequences([4,6,7,7]))