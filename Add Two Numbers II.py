class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = {}
        p2 = {}
        node1 = l1
        node2 = l2
        p1.update({l1:None, None:None})
        p2.update({l2:None, None:None})
        while node1.next:
            p1.update({node1.next:node1})
            node1 = node1.next
        while node2.next:
            p2.update({node2.next:node2})
            node2 = node2.next
        carry = 0
        result_node = None
        while node1 or node2:
            add1 = 0
            add2 = 0
            if node1:
                add1 = node1.val
            if node2:
                add2 = node2.val
            s = add1 + add2 + carry
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(s)
            node.next = result_node
            result_node = node
            node1 = p1[node1]
            node2 = p2[node2]
        return result_node

num1 = [7,2,4,3]
num2 = [5,6,4]
l1 = ListNode(num1[0])
node1 = l1
for i in range(1, len(num1)):
    node = ListNode(num1[i])
    node1.next = node
    node1 = node
l2 = ListNode(num2[0])
node2=l2
for i in range(1, len(num2)):
    node = ListNode(num2[i])
    node2.next = node
    node2 = node
Solution().addTwoNumbers(l1,l2)