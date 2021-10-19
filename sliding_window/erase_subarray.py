"""
Leetcode 1695. Maximum Erasure Value

This is a question that seems straight forward but a bit tricky. 

We need to update the window start when we find a duplicate.
Basically we need to keep updating the window_start value until the nums[window_start] = nums[window_end]

Usually in the sliding window formats, the while loop comes after updation. But here, if we follow the template, it is hard to implement.


"""

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        _sum = 0
        lookup = set()
        
        result = 0
        window_start = 0
        
        for window_end in range(len(nums)):
            
            while nums[window_end] in lookup:
                _sum -= nums[window_start]
                lookup.remove(nums[window_start])
                window_start += 1
            
            lookup.add(nums[window_end])
            _sum += nums[window_end]
            
            result = max(result, _sum)
        
        return result 

    