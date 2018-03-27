class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head_1 = None
        head_2 = None
        node_1 = head_1
        node_2 = head_2
        node = head
        while node:
            if node.val < x:
                if head_1:
                    node_1.next = node
                    node_1 = node
                else:
                    head_1 = node
                    node_1 = head_1
            else:
                if head_2:
                    node_2.next = node
                    node_2 = node
                else:
                    head_2 = node
                    node_2 = head_2
            node = node.next
        if node_1:
            node_1.next = head_2
        if node_2:
            node_2.next = None
        if head_1:
            return head_1
        else:
            return head_2

nums = [1]
head = ListNode(nums[0])
parent = head
for i in range(1, len(nums)):
    node = ListNode(nums[i])
    parent.next = node
    parent = node
solution = Solution()
head_ = solution.partition(head, 3)
node = head_
while node:
    print(node.val)
    node = node.next