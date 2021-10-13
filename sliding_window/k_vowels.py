"""
Leetcode 1456. Maximum Number of Vowels in a Substring of Given Length

Pretty straight forward solution 
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        window_start = 0
        result = 0
        match = 0
        
        for window_end in range(len(s)):
            
            if s[window_end] in vowels:
                match += 1
                
            if window_end - window_start +1 == k:
                
                result = max(result, match)
                
                if s[window_start] in vowels:
                    match -=1
                
                window_start += 1
                
        return result 