"""
1793. Maximum Score of a Good Subarray

Here the idea is 

 0  1  2  3  4  5
------------------
[1, 4, 3, 6, 4, 5] , K = 3 
------------------
 s  s  s  s
          e  e  e

Sub array start can take values <= 3 
Sub array end can take values >= 3 

So, start from each possible starting position, and iterate through different end positions is the brute force. 


But optimum approach will be starting from the Kth position and expand the window one by one. With that approach,
the array will be visited exactly once, and calculating minimum so far is also easy. With this approach, the condition

left <= K <= right is satified by default. 

[1, 4, 3, 6, 4, 5] , K = 3 

Score = 6, Left = 3, Right = 3, Min = 6

Consider two elements left and right to the Kth element. We need the max of min. So expand the window to the side
with maximum value. 

[1, 4, 3, 6, 4, 5] --> [1, 4, 3, 6, 4, 5] 
          ^                      ^
       ^     ^                ^        ^

There are two corner cases. To handle them, if left reaches 0th position, increment right.
If right reaches len(nums)-1, decrement left.

"""

from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        slow = 0 # 0 
        fast = k # 3
        min_so_far = 0
        score = 0 
        
        while slow <= k: # 1 < 3 
            
            while fast < len(nums): # 5 < 6 
                min_so_far = min(nums[slow:fast+1]) # nums[1:6]
                score = max(score, min_so_far * (fast-slow+1)) # 3 * (5-1+1) = 15
                fast += 1 # 5
            
            slow += 1 # 1 
            fast = k # 4
        
        return score 
        
    def maximumScore_Optimum(self, nums: List[int], k: int) -> int:
        
        left = right = k 
        min_so_far = nums[k]
        score = nums[k]
        
        while left > 0 or right < len(nums)-1: 
            
            if left == 0:
                right += 1
            elif right == len(nums) - 1:
                left -= 1
            elif nums[left-1] < nums[right+1]:
                right += 1
            else:
                left -= 1
                
            min_so_far = min(min_so_far, nums[left], nums[right])
            score = max(score, min_so_far * (right-left+1))  
         
        return score       
        