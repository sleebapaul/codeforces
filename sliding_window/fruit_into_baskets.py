"""

Leetcode 904. Fruit Into Baskets

My Idea: The concept of last seen 

Eg. [3,3,3,1,2,1,1,2,3,3,4]

Start from index 0 all the way to 3 we have the first streak which is 3, 3, 3, 1 

Now the next question is, where do I start the next streak? Obviously at 1. Which is last seen of 3 + 1 

How to find that index at which the next streak starts? 

last_seen = {fruit : index at which the fruit was last seen}
last_seen = {3:2, 1:3}

It is minimum of last seen values (farthest from the new fruit 2) => 2 

Next streak starts at 3

Eg. 1, 2, 1, 1, 1, 3, 3, 5, 5 

first window = 1, 2, 1, 1, 1 
last_seen = {1:4, 2:1}

So now, the next streak starts at 2 => min(4, 1) + 1 

"""


from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        last_seen = defaultdict()
        max_count = 0
        window_start = 0
        
        for window_end in range(len(fruits)): 
            last_seen[fruits[window_end]] = window_end 
            
            while len(last_seen) > 2:
                                
                first_elem_last_seen = min(last_seen.values()) 
                del last_seen[fruits[first_elem_last_seen]] 
                window_start = first_elem_last_seen + 1 

            max_count = max(max_count, window_end - window_start + 1)
                
        return max_count 
                