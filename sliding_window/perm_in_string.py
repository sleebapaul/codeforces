"""
Leetcode 567. Permutation in String

The idea is simple. First, put all the counts of pattern string in a hash map.

Whenever there is a char that is present in the pattern lookup, reduce the number by 1. If any element count becomes zero, that means, the criteria
for that character is met. Increment the number of matches by 1. 

Now, each time check if number of matches equals number of elements in hashmap. If yes, return True

Whenever the number of elements in the window greater than length of pattern string, there are two things to consider. 
1. If the character is in lookup and the count is zero, that means, it contributed to the number of matches. So reverse that effect by incrementing the matches. 
2. Increment the count in the hashmap by one as well. 

"""

from collections import defaultdict

class Solution:
    def checkInclusionBrute(self, pattern_string: str, s2: str) -> bool:
        
        k = len(pattern_string)
        n = len(s2)
        pattern_string = sorted(pattern_string)
        
        for i in range(n-k+1):
            window = sorted(s2[i:i+k])
            if pattern_string == window:
                return True
        return False
    
    def checkInclusion(self, pattern_string: str, s2: str) -> bool:
        
        k = len(pattern_string)
        n = len(s2)
        
        window_start = 0
        lookup = defaultdict(int)
        match = 0
        
        for i in range(k):
            lookup[pattern_string[i]] += 1 
                    
        for window_end in range(n):
            
            if s2[window_end] in lookup:
                lookup[s2[window_end]] -=1
                if lookup[s2[window_end]] == 0:
                    match +=1 
                
            if match == len(lookup):
                return True
            
            if window_end-window_start >= k-1:
                left_char = s2[window_start]
                window_start += 1

                if left_char in lookup:
                    if lookup[left_char] == 0:
                        match -= 1
                    lookup[left_char] += 1

        return False
            
            