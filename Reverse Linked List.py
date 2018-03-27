# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        node = head.next
        parent = head
        while node:
            next_node = node.next
            node.next = parent
            parent = node
            node = next_node
        head.next = None
        return parent

n = [1,2,3,4,5,6,7]
head = ListNode(n[0])
parent = head
for i in range(1, len(n)):
    node = ListNode(n[i])
    parent.next = node
    parent = node
solution = Solution()
solution.reverseList(head)