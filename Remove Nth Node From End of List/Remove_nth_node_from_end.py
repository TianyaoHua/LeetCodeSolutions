# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dictionary = {}
        current_node = head
        i = 1
        while current_node.next != None:
            dictionary.update({i: current_node})
            current_node = current_node.next
            i += 1
        dictionary.update({i:current_node})
        target = i - n + 1
        if target == 1 and head.next != None:
            return head.next
        elif target == 1 and head.next == None:
            return []
        elif target == i:
            previous_node = dictionary.get(target - 1)
            previous_node.next = None
        else:
            previous_node = dictionary.get(target - 1)
            next_node = dictionary.get(target + 1)
            previous_node.next = next_node
        return head


if __name__ == "__main__":
    solution = Solution()
    head1 = ListNode(0)
    head2 = ListNode(1)
    head3 = ListNode(2)
    head4 = ListNode(3)
    head1.next = head2
    head2.next = head3
    head3.next = head4
    head4.next = None
    answer = solution.removeNthFromEnd(head1, 1)
    node = answer
    while(node.next != None):
        print(node.val)
        node = node.next
    print(node.val)

