"""
Leetcode 424. Longest Repeating Character Replacement

My idea was to keep a while loop inside the for loop, and whenever 

while length(window) -  max(values in the count hash map) > k:
    reduce the window start element count by 1
    increase the window start by 1

But calculating the max in count hashmap is gonna be linear process. So the effective time complexity won't come down to O(n)

So the tricky part is calculating this max count inside the window, while adding an element to the count hashmap

Now the idea is, say for AAAAAABBBCC, the largest recurring element is A => 6 times. Now, whatever be the window in the rest of the array,
its length should be more than this value.

"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        largest_count_in_window = 0 
        window_start = 0
        max_len = 0 
        
        for window_end in range(len(s)):
            
            count[s[window_end]] += 1
            largest_count_in_window = max(largest_count_in_window, count[s[window_end]])
            
            if(window_end - window_start + 1 - largest_count_in_window) > k:
                
                count[s[window_start]] -= 1
                window_start += 1

            max_len = max(max_len, window_end - window_start + 1)
        
        return max_len