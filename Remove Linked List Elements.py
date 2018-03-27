# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        parent = ListNode('u')
        parent.next = head
        node = head
        superhead = parent
        while node:
            if node.val == val:
                parent.next = node.next
                node = node.next
            else:
                parent = node
                node = node.next
        return superhead.next
