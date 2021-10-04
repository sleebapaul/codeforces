"""
395. Longest Substring with At Least K Repeating Characters

This question is listed as a medium question under sliding window category.

But sliding window approach is too complex and maybe a hard problem for that case, simple approach is doing a dfs. 

But it is expensive. The following solution is not optimal but works. 

Time complexity -> O(N) for stack iteration, O(N) for set operation, O(N) for count operation. ==> O(N3) where N is the length of string 
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
                
        stack = [s]
        max_len = 0
        
        while stack:
            tmp = stack.pop()
            
            for key in set(tmp):
                if tmp.count(key) < k:
                    parts = tmp.split(key)
                    stack.extend(parts)
                    break
            else:
                max_len = max(max_len, len(tmp))
            
        return max_len 