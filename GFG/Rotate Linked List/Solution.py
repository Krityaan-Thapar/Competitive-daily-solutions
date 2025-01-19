class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def rotate(self, head, k):
        if head is None or head.next is None:
            return head
        
        l = 1
        tail = head
        while tail.next is not None:
            l += 1
            tail = tail.next
        
        k = k % l
        if k == 0:
            return head
        tail.next = head
        
        new_head = None
        new_tail = head
        while k - 1 > 0:
            new_tail = new_tail.next
            k -= 1
        
        new_head = new_tail.next
        new_tail.next = None
        return new_head