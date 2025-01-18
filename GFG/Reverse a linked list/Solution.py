class Solution:
    def reverseList(self, head):
        prev = None
        while head is not None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev