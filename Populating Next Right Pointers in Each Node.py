# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        Q = [root]
        n = 1
        while Q:
            for i in range(n):
                u = Q.pop(0)
                if u.left:
                    Q.append(u.left)
                if u.right:
                    Q.append(u.right)
            n = len(Q)
            for i in range(n-1):
                Q[i].next = Q[i+1]