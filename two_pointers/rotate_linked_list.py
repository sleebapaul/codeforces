"""
61. Rotate List

Find the length of list and connect the last node to first node 
Find the count == length - K, the next node will be the new head

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
     
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 0:
            return head 
        
        if head is None:
            return head 
        
        length = 1
        tmp = head

        while tmp.next:
            length += 1
            tmp = tmp.next
            
        tmp.next = head 
       
        k = k%length 
        
        new_head = None
        count = 0
        
        while head:
            count += 1
            
            if count == length-k:
                new_head = head.next
                head.next = None 
                break 
            else:
                head = head.next 
                
        return new_head 