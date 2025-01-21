class Solution:
    def reverseKGroup(self, head, k):
        ans = None
        l = 0
        
        prev = None
        prev_group_tail = None
        group_tail = head
        while head is not None:
            l += 1
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            
            if l == k:
                if ans is None:
                    ans = prev
                if prev_group_tail is not None:
                    prev_group_tail.next = prev
                
                prev_group_tail = group_tail
                group_tail = head
                prev = None
                l = 0
        if prev_group_tail is None:
            return prev
        prev_group_tail.next = prev
        return ans