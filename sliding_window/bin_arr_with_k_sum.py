"""
Leetcode 930. Binary Subarrays With Sum

Same logic as Leetcode 1248 and 992. 

It is hard to find out the exact K number using sliding windows. Same time, atmost K is kind of straight forward. 

"""

from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        return self.helper(nums, goal) - self.helper(nums, goal-1)
    
    def helper(self, nums, goal):
        
        window_start = 0 
        match = 0
        res = 0
        
        for window_end in range(len(nums)):
            
            if nums[window_end] == 1:
                match += 1
            
            while match > goal and window_start <= window_end:
                if nums[window_start] == 1:
                    match -= 1
                window_start += 1
            
            res += (window_end - window_start) + 1 
        
        return res 
            