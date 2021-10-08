"""
Leetcode 643. Maximum Average Subarray I

Typical sliding window problem
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_start = 0
        max_val = float("-inf")
        _sum = 0
        
        for window_end in range(len(nums)):
            _sum += nums[window_end]
            
            if window_end - window_start + 1 == k:
                avg = _sum/k
                max_val = max(max_val, avg)
                _sum -= nums[window_start]
                window_start += 1
        
        return max_val
            
        