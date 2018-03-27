# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serial = []
        if not root:
            return serial
        Q = [root]
        while Q:
            u = Q.pop(0)
            if u:
                serial.append(u.val)
                Q.append(u.left)
                Q.append(u.right)
            else:
                serial.append(None)
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        n = len(data)
        if not n:
            return None
        root = TreeNode(data[0])
        Q = [root]
        i = 1
        while i < n:
            q = len(Q)
            for j in range(q):
                u = Q.pop(0)
                if u:
                    value1 = data[i]
                    if value1 != None:
                        node = TreeNode(value1)
                        u.left = node
                        Q.append(node)
                    i += 1
                    value2 = data[i]
                    if value2 != None:
                        node = TreeNode(value2)
                        u.right = node
                        Q.append(node)
                    i += 1
        return root

solution = Codec()
root = TreeNode(-1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# root.left = node2
# node2.left = node3
# node3.left = node4
# node4.left = node5
root.left=TreeNode(0)
root.right=TreeNode(1)
print(solution.serialize(root))
solution.deserialize([-1, 0, 1, None, None, None, None])