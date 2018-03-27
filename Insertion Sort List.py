# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insert(self, node, end):
        head = node
        tail = end
        parent_node = None
        if node.val > node.next.val:
            head = node.next
        while parent_node != end:
            next_node = node.next
            if node.val > next_node.val:
                node.next = next_node.next
                next_node.next = node
                if parent_node:
                    parent_node.next = next_node
                parent_node = next_node
            else:
                tail = node
                break
        return head, tail
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head.next
        parent = head
        while node:
            next_node = node.next
            node.next = head
            head, tail = self.insert(node, parent)
            tail.next = next_node
            node = next_node
            parent = tail
        return head

