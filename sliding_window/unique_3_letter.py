"""
1876. Substrings of Size Three with Distinct Characters

This is quite a straight forward problem.

I tried using a last seen lookup but it is not the right way to do it. Just store the count in the lookup and that's enough
"""

from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        window_start = 0
        result = 0 
        lookup = defaultdict(int)
        
        for window_end in range(len(s)):                
            lookup[s[window_end]] += 1
            
            if window_end - window_start + 1 == 3:
                if len(lookup) == 3: 
                    result += 1
                lookup[s[window_start]] -= 1 
                if lookup[s[window_start]] == 0:
                    del lookup[s[window_start]]
                window_start += 1 
        return result 