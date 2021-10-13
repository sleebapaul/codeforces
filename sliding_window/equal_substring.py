"""
1208. Get Equal Substrings Within Budget

Straight forward. Asked the max len, so count the max  each time.
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        cost = 0
        window_start = 0
        
        result = 0
        
        for window_end in range(len(s)):
            
            cost += abs(ord(s[window_end]) - ord(t[window_end]))
            
            if cost > maxCost:
                cost -= abs(ord(s[window_start]) - ord(t[window_start]))
                window_start += 1 
            result = max(result, window_end - window_start+1)
        
        return result 