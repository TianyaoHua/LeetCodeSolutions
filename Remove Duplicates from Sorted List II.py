# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        grandparent = ListNode(-float('inf'))
        grandparent.next = head
        superhead = grandparent
        parent = head
        node = head.next
        flag = 0
        while node:
            if node.val == parent.val:
                parent.next = node.next
                node = node.next
                flag = 1
            else:
                if flag:
                    flag = 0
                    grandparent.next = node
                    parent = node
                    node = node.next
                else:
                    grandparent = parent
                    parent = node
                    node = node.next
        if flag:
            grandparent.next = node
        return superhead.next

nums = [0,1,1]
head = ListNode(1)
parent = head
for i in range(1, len(nums)):
    node = ListNode(nums[i])
    parent.next = node
    parent = node
solution = Solution()
a = solution.deleteDuplicates(head)
node = a
while node:
    print(node.val)
    node = node.next