# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even_head = head.next
        odd = ListNode(None)
        even = ListNode(None)
        node = head
        i = 1
        while node:
            if i%2:
                odd.next = node
                odd = node
            else:
                even.next = node
                even = node
            node = node.next
            i += 1
        even.next = None
        odd.next = even_head
        return head

solution = Solution()
nums = [1,2,3,4,5,6,7]
head = ListNode(nums[0])
parent = head
for i in range(1, len(nums)):
    node = ListNode(nums[i])
    parent.next = node
    parent = node
solution.oddEvenList(head)