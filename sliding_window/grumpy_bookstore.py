"""
1052. Grumpy Bookstore Owner

It is a tricky question. At first, I thought it is similar to Leetcode 1004. Max Consecutive Ones III

But the minutes given in the question is consecutive. That means, the window size is the minutes. 

The idea is, first calculate the number of customers who will be definitely happy, which means when owner is not grumpy.

Now to find the max sum subarray with width minutes, and add it to the previous value. 

While doing it, remember to consider only of customers that have come when the owner is grumpy.

"""
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        window_start = 0 
        res = 0
        _sum = 0 
        
        satisfied_customers = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]
        
        for window_end in range(len(grumpy)):
            
            if grumpy[window_end] == 1:
                _sum += customers[window_end]
            
            while window_end - window_start + 1 >= minutes:
                res = max(res, _sum)
                if grumpy[window_start] == 1:
                    _sum -= customers[window_start]
                
                window_start += 1
        
        return res + satisfied_customers