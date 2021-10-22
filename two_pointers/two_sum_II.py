"""
Leetcode 167. Two Sum II - Input array is sorted

Two pointer problem. Slow pointer at 0 and fast pointer at len(nums)-1

"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        slow = 0
        fast = len(numbers)-1
        
        while slow < fast:
            
            _sum = numbers[slow] + numbers[fast]
            
            if _sum == target:
                return [slow+1, fast+1]
            
            elif _sum > target:
                fast -= 1
            
            else:
                slow += 1