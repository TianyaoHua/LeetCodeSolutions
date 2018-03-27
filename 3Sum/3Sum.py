class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        collection = {}
        answer = []
        for i in nums:
            if i not in collection:
                collection[i]=0
            collection[i] += 1
        unique = collection.keys()
        positive = sorted(i for i in unique if i > 0)
        non_positive = sorted(i for i in unique if i <= 0)
        if collection.get(0) > 2:
            answer.append([0,0,0])
        for i in positive:
            for j in non_positive:
                target = -(i + j)
                if target in collection:
                    if (target == i or target == j)and collection.get(target)>1:
                        answer.append([j, target, i])
                    elif target > 0 and target > i:
                        answer.append([j, target, i])
                    elif j < target <=0:
                        answer.append([j, target, i])
        return answer
if __name__ == "__main__":
    solution = Solution()
    answer = solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    print(answer)
