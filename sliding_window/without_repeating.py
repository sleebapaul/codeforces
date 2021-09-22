"""
Leetcode 3. Longest Substring Without Repeating Characters

The idea is similar to k unique longest substring. 

But there is a catch. Take the word "abba" 

Here the window starts at 0, b is repeated, so there the window start needs to be updated. We keep a hashmap to keep track of the last seen indices of each char. 

So at second b, last_seen = {a: 0, b: 1}
Now window_start = last_seen[b]. But this is wrong. Because, what comes next is a. 

a is already in the last_seen, then window_start will go back to 0. Which is wrong. 

So whenever repeating chars are found, window_start = max(window_start, last_seen[char]+1)

"""

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        
        last_seen = defaultdict(int)
        max_len = 0
        window_start = 0
        
        for window_end in range(len(s)): 
            
            if s[window_end] in last_seen: 
                window_start = max(window_start, last_seen[s[window_end]] + 1)  
            max_len = max(max_len, window_end - window_start + 1) 
            last_seen[s[window_end]] = window_end
            
        return max_len 