"""
Leetcode 438. Find All Anagrams in a String

The idea is exactly the same as Leetcode 567. Permutation in String as anagram just another name for permutation. 

Just keep adding the window start indices to the results, when the number of matches equals the length of lookup


"""

from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        lookup = defaultdict(int)
        
        for val in p:
            lookup[val] +=1 
            
        window_start = 0
        match = 0
        result = []
        
        for window_end in range(len(s)):
            
            if s[window_end] in lookup:
                lookup[s[window_end]] -= 1
                
                if lookup[s[window_end]] == 0:
                    match += 1
            
            if match == len(lookup):
                result.append(window_start)
            
            if window_end - window_start + 1 >= len(p):
                
                if s[window_start] in lookup:
                    if lookup[s[window_start]] == 0:
                        match -=1
                    lookup[s[window_start]] += 1
                
                window_start += 1
                
        return result 
            
        