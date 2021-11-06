"""

31. Next Permutation

Finding the next lexicographical permutation

Step 1: Start from right because we will be altering the positions from most right possible 

Step 2: Find the index at which the previous element is lexicographically less than current element. Let's 
call this the pivot index and previous index. 

Step 3: Now, starting from pivot index to the right of array upto the end, find the element that is greater 
than the previous index element and also the right most. Let's call it swap index. 

Step 4: Swap the previous index element and swap index element

Step 5: Reverse the array starting from pivot element to the end 

If step 2 is never found, the array is already at the maximum position. Reverse to start from the beginning.

i.e. [3,2,1] -> [1,2,3]

.reverse() gives inplace reverse in Python

"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for last_idx in range(len(nums)-1, 0, -1):
            
            if nums[last_idx-1] < nums[last_idx]:
                
                swap_idx = last_idx
                
                # Find an element greater than nums[last_idx-1] and farthest from the last_idx-1
                
                for j in range(last_idx, len(nums)):
                    if nums[j] > nums[last_idx-1]:
                        swap_idx = j 
                
                # Swap the elements 
                
                nums[last_idx-1], nums[swap_idx] = nums[swap_idx], nums[last_idx-1]
                
                # Now reverse the elements past the last_idx
                
                nums[last_idx:] = nums[last_idx:][::-1]
                
                return nums
        
        return nums.reverse()

