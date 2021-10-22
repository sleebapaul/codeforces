"""

Leetcode 451. Sort Characters By Frequency

Naive way: Store frequencies in the hashmap. Put everything on a maxheap. Pop out one by one. 
Time: O(NlogN) 
Space: O(N)

Bucket Sort 

Create an array of buckets. Put the characted in the bucket with position as frequency. 
From reverse, get elements and keep adding to result 

"""

from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        
        lookup = defaultdict(int)
        result = ""
        
        for val in s:
            lookup[val] += 1
        
        buckets = [None for x in range(len(s))]
        
        for k, v in lookup.items():
            if buckets[v-1] is None:
                buckets[v-1] = []
            
            buckets[v-1].append(k)
        
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                for letter in buckets[i]:
                    tmp = (i+1) * letter
                    result += tmp
        
        return result
            
        