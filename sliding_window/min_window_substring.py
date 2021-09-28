"""

Leetcode 76. Minimum Window Substring

Same idea of string permutation Leetcode 567. Permutation in String

But here, whenever number of matches equals the length of lookup, we need to increment the start of the window until match is less. 

Eg. 

"ADOBECODEBANC", t = "ABC"

First match = "ADOBEC"

Now the window has to start from "B" i.e. "BEC". For that, we keep iterating until number of matches not equals length of lookup. 
We don't really care about the letters which are not in the lookup, in this case "DO"
"""


from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        lookup = defaultdict(int)
        
        for val in t:
            lookup[val] +=1 
            
        window_start = 0
        match = 0
        result = ""
        result_len = float("inf")
        
        for window_end in range(len(s)):
            
            if s[window_end] in lookup:
                lookup[s[window_end]] -= 1
                
                if lookup[s[window_end]] == 0:
                    match += 1
            
            while match == len(lookup):
                
                if window_end - window_start + 1 < result_len:
                    result = s[window_start:window_end+1]
                    result_len = window_end - window_start + 1 
                            
                if window_end - window_start + 1 >= len(t):

                    if s[window_start] in lookup:
                        if lookup[s[window_start]] == 0:
                            match -= 1
                        lookup[s[window_start]] += 1

                    window_start += 1
                
        return result 
        