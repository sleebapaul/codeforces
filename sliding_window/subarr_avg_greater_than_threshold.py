"""
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Typical sliding window question 

"""

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_start = 0
        _sum = 0
        result = 0
        
        for window_end in range(len(arr)):
            _sum += arr[window_end]
                                
            if window_end - window_start + 1  == k:
                if _sum/k >= threshold :
                    result += 1
                
                _sum -= arr[window_start]                    
                window_start += 1 
                        
        return  result 