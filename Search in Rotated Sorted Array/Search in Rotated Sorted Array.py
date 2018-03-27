class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


if __name__ == "__main__":
    solution = Solution()
    # for i in [4,5,6,7,0,1,2,-float('inf'),float('inf')]:
    #     index = solution.search([4,5,6,7,0,1,2],i)
    #     print(index)
    index = solution.search([2,3,4,5,6,7,8,9,1],9)
    print(index)