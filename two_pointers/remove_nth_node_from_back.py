"""

19. Remove Nth Node From End of List

Can be solved using the fast and slow pointer as well. 
Used the similar strategy of first finding the length of the list.

If n == length, that means first element needs to be popped. That's a corner case. 

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:   
        
        if head is None:
            return head 

        length = 0
        tmp = head
        
        while tmp:
            length +=1 
            tmp = tmp.next 
            
        if length == n:
            return head.next 
        
        position = 0 
        
        tmp = head
        
        while length - n - 1  != position:
            tmp = tmp.next 
            position += 1 

        tmp.next = tmp.next.next 
        
        return head 
            