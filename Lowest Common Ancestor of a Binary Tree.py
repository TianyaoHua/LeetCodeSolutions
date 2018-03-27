# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def BFS(self, root, parent):
        Q = [root]
        while Q:
            u = Q.pop(0)
            if u.left:
                Q.append(u.left)
                parent[u.left] = u
            if u.right:
                Q.append(u.right)
                parent[u.right] = u
        return parent

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {}
        self.BFS(root, parent)
        p_parent = p
        parent_for_p = set()
        while p_parent != root:
            parent_for_p.update({p_parent})
            p_parent = parent[p_parent]
        parent_for_p.update({root})
        q_parent = q
        while q_parent not in parent_for_p:
            q_parent = parent[q_parent]
        return q_parent
