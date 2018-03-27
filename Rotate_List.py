class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not (k and head and head.next):
            return head
        current_node = head
        n = 0
        while current_node:
            current_node = current_node.next
            n += 1
        k = k % n
        for i in range(k):
            current_node = head
            while current_node.next.next:
                current_node = current_node.next
            tail = current_node.next
            current_node.next = None
            tail.next = head
            head = tail
        return head


if __name__ == "__main__":
    x = [1,2,3]
    nodes = []
    for i in range(len(x)):
        node = ListNode(x[i])
        nodes.append(node)
    for i in range(len(x)-1):
        nodes[i].next = nodes[i+1]
    nodes[len(nodes)-1].next = None
    head = nodes[0]
    solution = Solution()
    head_ = solution.rotateRight(head,200000)
    current_node = head_
    while current_node:
        print(current_node.val)
        current_node = current_node.next


