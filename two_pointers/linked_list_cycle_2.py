"""
142. Linked List Cycle II

Similar idea of 287. Find the Duplicate Number

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        if head.next is None:
            return None 
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        
        if not fast or not fast.next: return None
        
        fast = head
                
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow 
        
        
        
        
        