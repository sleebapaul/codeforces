"""
Leetcode 978. Longest Turbulent Subarray

The idea is pretty straight forward. If there are duplicates, keep increasing the window start pointer. 
Otherwise, check if the conditions given in the question is valid and keep expanding the window end pointer.
Once a valid window is found, reset the pointers. 

Idea from the leetcode discussion

"""

from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        if len(arr) == 1:
            return 1
        
        window_start, window_end, res = 0, 0, 0
        
        while window_end < len(arr):
            
            while window_start < len(arr)-1 and arr[window_start] == arr[window_start+1]:
                window_start += 1
            
            while window_end < len(arr)-1 and (arr[window_end-1] < arr[window_end] > arr[window_end+1] or arr[window_end-1] > arr[window_end] < arr[window_end+1]):
                window_end += 1 
            
            res = max(res, window_end-window_start+1)
            window_start = window_end
            window_end += 1
            
        return res 
            