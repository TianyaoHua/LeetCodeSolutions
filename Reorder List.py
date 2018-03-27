# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        array = []
        node = head
        while node:
            array.append(node)
        n = len(array)
        if not n%2:
            i = -1
            for i in range(n//2-1):
                array[i].next = array[n-1-i]
                array[n-1-i].next = array[i+1]
            i += 1
            array[i].next = array[i+1]
            array[i+1].next = None
        else:
            i = -1
            for i in range(n//2):
                array[i].next = array[n-1-i]
                array[n-1-i].next = array[i+1]
            array[i+1].next = None

