class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.size = 1
        self.p = None
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, node):
        y = None
        x = root
        r = 0
        while x:
            y = x
            if node.val <= x.val:
                x.size += 1
                x = x.left
            else:
                if x.left:
                    r += x.left.size + 1
                else:
                    r += 1
                x.size += 1
                x = x.right
        node.p = y
        if not y:
            root = node
        elif node.val <= y.val:
            y.left = node
        else:
            y.right = node
        return root, r

    # def rank(self, root, node):
    #     r = 1
    #     y = node
    #     while y != root:
    #         if y == y.p.right:
    #             r = r + y.p.left.size+1
    #         y = y.p
    #     return r


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if not n:
            return []
        else:
            counter = [0 for i in range(n)]
            counter[-1] = 0
            root = TreeNode(nums[-1])
            for i in range(n-2, -1, -1):
                node = TreeNode(nums[i])
                root, r = self.insert(root, node)
                counter[i] = r
        root = root

        return counter

solution = Solution()
nums = [1,2,1,2,1,2,1]
counter = solution.countSmaller(nums)
print(counter)
