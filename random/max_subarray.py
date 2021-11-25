"""

53. Maximum Subarray

Typical Kedane's algorithm problem

"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_ending_here = 0 
        max_so_far = float("-inf")
        
        for i in range(len(nums)):
            
            max_ending_here += nums[i]
            
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            
            if max_ending_here < 0:
                max_ending_here = 0
        
        return max_so_far