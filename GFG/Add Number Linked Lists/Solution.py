class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverseLL(self, head):
        prev = None
        while head is not None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
    
    def addTwoLists(self, num1, num2):
        if num1 is None and num2 is None:
            return Node(0)
        
        if num1 is None:
            return num2
        
        if num2 is None:
            return num1
        
        carry = 0
        num1 = tmp1 = self.reverseLL(num1)
        num2 = tmp2 = self.reverseLL(num2)
        prev1 = None
        
        while num1 is not None and num2 is not None:
            s = carry + num1.data + num2.data
            carry = s // 10
            s = s % 10
            
            num1.data = s
            prev1 = num1
            num1 = num1.next
            num2 = num2.next
        
        while num1 is not None:
            s = carry + num1.data
            carry = s // 10
            s = s % 10
            
            prev1 = num1
            num1.data = s
            num1 = num1.next
        
        while num2 is not None:
            s = carry + num2.data
            carry = s // 10
            s = s % 10
            
            prev1.next = Node(s)
            prev1 = prev1.next
            num2 = num2.next
            
        if carry > 0:
            prev1.next = Node(carry)
            prev1 = prev1.next
        prev1.next = None
        
        ans_head = self.reverseLL(tmp1)
        while ans_head.data == 0:
            ans_head = ans_head.next
        return ans_head