"""
350. Intersection of Two Arrays II

What if the given array is already sorted? How would you optimize your algorithm?

- Use intersect_three 
- Time: O(M+N)
- Space: O(1)

What if nums1's size is small compared to nums2's size? Which algorithm is better?

- Use intersect_two
- Time: O(M+N)
- Space: O(min(M, N))

What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

- Modify intersect_two if nums1 can be stored in memory as hashmap
- Yield nums2 in chunks and iterate

What is both of the arrays don't fit in the memory?

- Yield nums1 in chunks and create the lookup
- Yield nums2 in chunks and follow intersect_two


"""

from collections import defaultdict
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        
        counter_nums1 = defaultdict(int)
        for val in nums1:
            counter_nums1[val] +=1 
        
        counter_nums2 = defaultdict(int)
        for val in nums2:
            counter_nums2[val] +=1 
            
        for k, v in counter_nums1.items():
            if k in counter_nums2.keys():
                res.extend(min(v, counter_nums2[k])*[k])
        
        return res

    
    def intersect_two(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Optimized version of intersect

        Args:
            nums1 (List[int]): First array
            nums2 (List[int]): Second array

        Returns:
            List[int]: Array of common elements
        """

        if len(nums1) > len(nums2) : self.intersect_two(nums2, nums1)
        
        res = []
        
        counter_nums1 = defaultdict(int)
        for val in nums1:
            counter_nums1[val] +=1 
            
        for val in nums2:
            if counter_nums1[val] > 0:
                res.append(val)
                counter_nums1[val] -= 1
        
        return res


    def intersect_three(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        res = []

        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(nums1) and ptr2 < len(nums2):

            if nums1[ptr1] == nums2[ptr2]:
                res.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1 
        
        return res