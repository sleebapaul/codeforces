"""
Leetcode 1297. Maximum Number of Occurrences of a Substring

The way is pretty straight forward. We need to keep track of two things. 

1. Is the string contain the unique numbers < maxLetters (Using the lookup)
2. The window length is minSize. (Using if loop)

Why not maxSize? Because it is asked the max count of repeating substring. So obviously, the minSize window width meets the criteria. 

Find the max count key from the resulting dictionary 

Time complexity: O(NK)
Space complexity: O(N)
"""

from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
                
        window_start = 0
        match = 0
        result = defaultdict(int)
        lookup = defaultdict(int)
        
        for window_end in range(len(s)):
            
            if s[window_end] not in lookup:
                match += 1 
                
            lookup[s[window_end]] += 1 
                
            if window_end - window_start + 1  == minSize:
                if match <= maxLetters :
                    result[s[window_start:window_end+1]] += 1 
                    
                lookup[s[window_start]] -= 1
                
                if lookup[s[window_start]] == 0:
                    match -= 1
                    del lookup[s[window_start]]                       
                window_start += 1 
                        
        return  max(result.values()) if result else 0