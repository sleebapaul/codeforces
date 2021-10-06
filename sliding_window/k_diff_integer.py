"""
Leetcode 992. Subarrays with K Different Integers

The idea is the same for many problems similar to K exact or K distinct etc. 

It is hard to find out the exact K number using sliding windows. Same time, atmost K is kind of straight forward. 

So, we find the difference between K atmost and K-1 atmost. 

"""

from collections import defaultdict
from typing import List

class Solution:
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        return self.helper(nums, k) - self.helper(nums, k-1)
    
    def helper(self, nums, k):
        
        window_start = 0
        result = 0
        lookup = defaultdict(int)
        match = 0
        
        for window_end in range(len(nums)):
            
            if nums[window_end] not in lookup:
                match += 1
                
            lookup[nums[window_end]] +=1 
            
            while match > k:
                
                lookup[nums[window_start]] -= 1
                if lookup[nums[window_start]] == 0:
                    match -= 1
                    del lookup[nums[window_start]]
                
                window_start += 1
            
            result += (window_end - window_start) 
                
        return result 