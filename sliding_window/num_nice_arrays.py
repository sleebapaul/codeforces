"""
Leetcode 1248. Count Number of Nice Subarrays
Leetcode 992. Subarrays with K Different Integers


The idea is the same for many problems similar to K exact or K distinct etc. 

It is hard to find out the exact K number using sliding windows. Same time, atmost K is kind of straight forward. 

So, we find the difference between K atmost and K-1 atmost. 

"""
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k-1)
    
    def helper(self, nums, k):
        
        window_start = 0
        result = 0
        match = 0
        
        for window_end in range(len(nums)):
            
            if nums[window_end] %2 == 1:
                match += 1
                            
            while match > k:
                if nums[window_start]%2 == 1:
                    match -= 1
                    
                window_start += 1
            
            result += (window_end - window_start) 
                
        return result 