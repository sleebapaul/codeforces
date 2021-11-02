"""
16. 3Sum Closest

Idea can be adopted from 3Sum problem. Here we need to return the closest sum, so no need to keep records of all the combinations

The left and right pointers are moved based on distance between sum and target. In 3Sum it is based on just sum.

Time: O(N2)

"""


from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        distance = float("inf")
        closest = 0
        
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            
            while l<r:
                _sum = nums[i] + nums[l] + nums[r]
                
                if _sum == target:
                    return target
                                
                if  abs(_sum - target) < distance:
                    closest = _sum
                    distance =  abs(_sum - target)
                
                if _sum - target < 0:
                    l+=1
                else:
                    r-=1
            
        return closest

