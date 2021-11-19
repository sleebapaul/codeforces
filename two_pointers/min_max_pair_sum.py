"""
1877. Minimize Maximum Pair Sum in Array

Pretty straight forward. Min of Max means map min and max in each pair. 

Eg. [3, 5, 2, 3]

Sort it => [2,3,3,5]
Pairs => (1,5), (3,3)
Max of pair sum => max(6, 6) = 6 

"""

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        left = 0
        right = len(nums)-1
        
        scores = []
        
        while left <= right:
            scores.append(nums[left] + nums[right])
            left += 1
            right -= 1
        
        return max(scores)