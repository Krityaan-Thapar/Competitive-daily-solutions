class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def sortedMerge(self, head1, head2):
        one = head1
        two = head2
        sentinel = Node(-1)
        curr = sentinel
        
        if one is None and two is None:
            return None
        if one is None:
            return two
        if two is None:
            return one
        
        while one is not None and two is not None:
            if one.data <= two.data:
                curr.next = one
                one = one.next
                curr = curr.next
            else:
                curr.next = two
                two = two.next
                curr = curr.next
        
        if one is not None:
            curr.next = one
        if two is not None:
            curr.next = two
        
        return sentinel.next