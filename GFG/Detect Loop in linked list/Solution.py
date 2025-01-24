class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Solution:
    def detectLoop(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False