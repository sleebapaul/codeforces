"""
287. Find the Duplicate Number

Very interesting problem. 

At first glance it is a very straight forward problem. But the constraints in the solution make it interesting. 

There are time complexity of O(N) solutions available. But making it constant memory, is tough. 

So there is an XOR trick which can be used. Following features of XOR are going to be helpful

x ^ x = 0
x ^ 0 = x 

-> With XOR

Find the range of the the array. Min and Max. Here in the question, the range is defined from 1 to N

Consider the array, [1, 3, 4, 2, 2], range is 1 to 4

Now, (1^3^4^2^2) ^ (0^1^2^3^4) --> 2 

So in a loop, result = result ^ array[i] ^ i should do the work. 

But this is now enough for the test case [2,2,2]

Now we have an interesting concept coming here. Think about cycles. 

Use a fast and slow pointer. Slow travels one step at a time, fast travels two. 

A step is defined as the situation. Here it is index. 

array = [1, 3, 4, 2, 2]

slow = 1 => nums[0]
fast = 3 => nums[nums[0]]

Now follow the cycle. 

Slow ---> 1 -> 3 -> 2 -> 4 
Fast ---> 3 -> 4 -> 4 -> 4 

Now what we understand here is, the entry point to the cycle is the repeating term. 

Now we need to find that entry point element. For that we can restart the fast point from the left most index 
and travel similar to slow pointer. 

Slow --->  2 -> 4 -> 2 
Fast ----> 1 -> 3 -> 2 

2 is the answer

Similar idea on LC 142. Linked List Cycle II

"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[nums[0]]
        
        # Stop where the cycle starts 
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = 0
        # Find the entry point by starting from the left most index
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow 
        