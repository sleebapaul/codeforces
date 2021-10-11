"""
Leetcode 1031. Maximum Sum of Two Non-Overlapping Subarrays

Sliding window idea from the leetcode discuss 

1. There are two possibilities
    - The window with length of secondLen goes first 
    - The window with length of firstLen goes second 
    - And vice versa

2. We find the maximum window sum generated in by the first window and keep it 
3. In the second iteration, we take the other situation and find the max window sum 
4. To keep the sum calculation easy, we use a prefix sum array 

"""

from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        first_len_window_max = 0 
        prefix_sum = [0]
        
        result = 0
        
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
                
        # firstLen followed by secondLen [ _ ]  and [ _ _ ] 
        first_len_max = 0
        for i in range(firstLen+secondLen, len(prefix_sum)):
            
            range_sum_firstLen = prefix_sum[i-secondLen] - prefix_sum[i-firstLen-secondLen]
            range_sum_secondLen= prefix_sum[i] - prefix_sum[i-secondLen]
            
            first_len_max = max(first_len_max, range_sum_firstLen)
            result = max(result, first_len_max + range_sum_secondLen)
            
        # secondLen followed by firstLen [ _ _ ]  and [ _ ] 
        second_len_max = 0
        for i in range(firstLen+secondLen, len(prefix_sum)):
            
            range_sum_firstLen = prefix_sum[i] - prefix_sum[i-firstLen]
            range_sum_secondLen = prefix_sum[i-firstLen] - prefix_sum[i-firstLen-secondLen]
            
            second_len_max = max(second_len_max, range_sum_secondLen)
            result = max(result, second_len_max + range_sum_firstLen)
            
        return result
    