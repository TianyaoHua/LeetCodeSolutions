class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree(self, nums, p, q):
        if q > p:
            middle = (p+q)//2
            node = TreeNode(nums[middle])
            node.left = self.tree(nums, p, middle-1)
            node.right = self.tree(nums, middle+1, q)
        elif q == p:
            node = TreeNode(nums[p])
            node.left = None
            node.right = None
        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.tree(nums,0,len(nums)-1)
        return root

nums = [-10,-3,0,5,9]
solution = Solution()
solution.sortedArrayToBST(nums)
