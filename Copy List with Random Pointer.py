# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        h1 = {}
        h2 = {}
        head_c = RandomListNode(head.label)
        parent = head_c
        h1.update({head_c: head})
        h2.update({head: head_c})
        node = head.next
        while node:
            node_c = RandomListNode(node.label)
            h1.update({node_c: node})
            h2.update({node: node_c})
            parent.next = node_c
            node = node.next
            parent = node_c
        h1.update({None: None})
        h2.update({None: None})
        node_c = head_c
        while node_c:
            print(h1[node_c].label)
            node_c.random = h2[h1[node_c].random]
            node_c = node_c.next
        return head_c

head = RandomListNode(-1)
node = RandomListNode('#')
head.next = node
head.random = node
solution = Solution()
solution.copyRandomList(head)