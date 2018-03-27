# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insert(self, head, node):
        x = head
        y = None
        while x and node.val > x.val:
            y = x
            x = x.right
        node.left = None
        node.right = x
        if y:
            y.right = node
        else:
            head = node
        return head

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        Q = [root]
        d = {0: [root]}
        h = 0
        while Q:
            n = len(Q)
            h += 1
            for i in range(n):
                u = Q.pop(0)
                if u.left:
                    if h not in d:
                        d.update({h:[]})
                    d[h].append(u.left)
                    Q.append(u.left)
                if u.right:
                    if h not in d:
                        d.update({h:[]})
                    d[h].append(u.right)
                    Q.append(u.right)
        root.left = None
        root.right = None
        for i in range(1, h+1):
            for node in d[i]:
                root = self.insert(root, node)


