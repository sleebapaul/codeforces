"""
Leetcode 1004. Max Consecutive Ones III

My idea derived from Leetcode 424. Longest Repeating Character Replacement

In 424, we don't know the content of the window, so we keep updating the largest_count_in_window
But here, we know it is just zeros and ones. So, keep adding the count.

While the count[0]>k, we keep increasing the window_start. 

But this not the optimum solution as the while loop, at work can run upto O(n-k).

We may follow the solution in 424. But largest_count_in_window is updated only when the nums[i] is 1. And it is reduced by one, whenever the zeros count > k

"""


from collections import defaultdict
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        window_start = 0
        max_len = 0
        count = defaultdict(int)
        
        for window_end in range(len(nums)):
            
            count[nums[window_end]] += 1
            
            while count[0] > k:    
                count[nums[window_start]] -= 1
                window_start += 1 
              
            max_len = max(max_len, window_end - window_start + 1)
            
        return max_len

    def longestOnesOpt(self, nums: List[int], k: int) -> int:
        
        window_start = 0
        max_len = 0
        largest_count_in_window = 0
        
        for window_end in range(len(nums)):
            
            if nums[window_end] == 1:
                largest_count_in_window += 1
            
            if (window_end - window_start + 1 - largest_count_in_window) >  k:  
                if nums[window_start] == 1:
                    largest_count_in_window -= 1
                window_start += 1 
              
            max_len = max(max_len, window_end - window_start + 1)
            
        return max_len
                