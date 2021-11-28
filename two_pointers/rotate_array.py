"""
189. Rotate Array

"""

from typing import List

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time: O(N)
        Space: O(1)

        Reverse last K elements 
        Reverse the first N-K elements 
        Reverse the whole array 

        
        """
        
        def reverse_array(nums, i, j):
            
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        n = len(nums)
        k %= len(nums)
        reverse_array(nums, n-k, n-1)
        reverse_array(nums, 0, n-k-1)
        reverse_array(nums, 0, n-1)
        return

    
    def rotate(self, nums: List[int], k: int) -> None:

        """

        Time: O(kN)
        Space: O(1)
        
        """

        for _ in range(k):
            tmp  = nums[0]
            for i in range(1, len(nums)):
                
                nums[i], tmp = tmp, nums[i]
                
                if i == len(nums) - 1:
                    nums[0] = tmp
        return 

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Time: O(N)
        Space: O(N)
        
        """

        result = [0]*len(nums)
        for i in range(len(nums)):
            new_pos = k + i 
            if new_pos >= len(nums):
                new_pos = new_pos%len(nums)
            
            result[new_pos] = nums[i]
        
        return result 