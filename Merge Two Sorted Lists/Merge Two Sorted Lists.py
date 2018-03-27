# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current_node = head
        current_node_1 = l1
        current_node_2 = l2
        while current_node_1 and current_node:
            if current_node_1.val < current_node_2.val:
                current_node.next = current_node_1
                current_node_1 = current_node_1.next
            else:
                current_node.next = current_node_2
                current_node_2 = current_node_2.next
        if current_node_2 != None:
            current_node.next = current_node_2
        if current_node_1 != None:
            current_node.next = current_node_1
        return head.next
if __name__ == "__main__":
    solution = Solution()
    ansewr = solution([])