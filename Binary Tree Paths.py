# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def DFS(self, u, answer, solution):
        answer += str(u.val)+'->'
        if u.left:
            self.DFS(u.left, answer, solution)
        if u.right:
            self.DFS(u.right, answer, solution)
        if not (u.left or u.right):
            solution.append(answer[0:-2])

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        answer = ''
        solution = []
        self.DFS(root, answer, solution)
        return solution

root = TreeNode(1)
leaf = TreeNode(2)
root.left = leaf
solution = Solution()
print(bool(root.left and root.right))
print(solution.binaryTreePaths(root))