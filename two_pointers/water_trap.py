"""
42. Trapping Rain Water

The fundamental idea is all about finding how to calculate the height of water that can be stored in a particular index. 

The stored water will be depending upon the left max level and right max level 
Also current level should be less than these max levels otherwise the water cannot be stored.

 __    __           __ __ __
|  |__|  |  ---> 1 |  |  |  | ---> 0

Another idea to noted down is, the water that can be stored based on min(left max, right max). Otherwise the water will spill away.
       __
 __   |  |
|  |__|  | Here the maximum capacity is 1 not 2 

So water_stored[i] = min(left_max_level, right_max_level) - current_level


Method 1 : Store the right max and left max for all the indices and use the formula (DP)

Method 2 : Do it in a single pass using two pointers

We can say that if there is a larger bar at one end (say right), we are assured that 
the water trapped would be dependant on height of bar in current direction (from left to right). 
As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left). We must maintain 
left_max and right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.

"""
from typing import List

class Solution:

    def trap_opt(self, height:List[int]) -> int:

        result = 0 
        left_max_arr = [0]*len(height)
        right_max_arr = [0]*len(height)

        left_max_arr[0] = height[0]
        right_max_arr[-1] = height[-1]

        for i in range(1, len(height)):
            left_max_arr[i] = max(height[i], left_max_arr[i-1])
        
        for j in range(len(height)-2, -1, -1):
            right_max_arr[j] = max(height[j], right_max_arr[j+1])
        
        for k in range(len(height)):
            result += min(left_max_arr[k], right_max_arr[k]) - height[k]

        return result

    def trap(self, height: List[int]) -> int:
        
        left = 0 
        right = len(height)-1
        
        left_max = height[left]
        right_max = height[right]
        
        result = 0
        
        while left < right:
            if height[left] < height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1
        
        return result 