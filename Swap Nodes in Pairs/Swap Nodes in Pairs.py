# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        else:
            current_node = head
            next_node = head.next
            previous_node = ListNode(0)
            previous_node.next = head
            pre_head = previous_node
            while  next_node and  current_node:
                previous_node.next = next_node
                current_node.next = next_node.next
                next_node.next = current_node
                previous_node = current_node
                current_node = current_node.next
                if current_node:
                    next_node = current_node.next
                node1 = pre_head
        return pre_head.next

if __name__ == "__main__":
    head = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n3.next = None
    n4.next = None
    solution = Solution()
    answer = solution.swapPairs(head)
    node = answer
    while node:
        print(node.val)
        node = node.next