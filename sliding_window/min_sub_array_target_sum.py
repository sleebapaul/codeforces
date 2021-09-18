"""
Leetcode 209. Minimum Size Subarray Sum

Optimized solution my idea: 

When the sum is greater than or equals to target, update the min_count.
But there is an edge case where, the main loop could end, but still there is elements left in array which could yield a better min_count. 
So convert the "if" to a while loop, which will keep increasing the left most index when window sum is greater than or equals  target

"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        count = float("inf")
        
        for i in range(len(nums)):
            tmp_sum = 0
            for j in range(i, len(nums)):
                tmp_sum += nums[j]
                if tmp_sum >= target:
                    count = min(count, j-i+1)

        return count if count < float("inf") else 0

    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        count = float("inf")
        window_sum = 0
        window_start_idx = 0
        
        for window_end in range(len(nums)):
            window_sum += nums[window_end]              
            
            while window_sum >= target:
                count = min(count, window_end - window_start_idx+1)
                window_sum -= nums[window_start_idx]
                window_start_idx += 1
            
        return count if count < float("inf") else 0

