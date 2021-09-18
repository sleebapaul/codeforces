"""
Leetcode premium question - Longest Substring with K Distinct Characters

Idea is very similar to Leetcode 209. Minimum Size Subarray Sum

We need a hashmap to save the array values and their counts. Whenever the length of lookup is greater than K, we do the following steps.

1. Calculate the max len by taking the difference between window start and end 
2. Now we need to update window start. It is easy. That will be number of occurances of left most element in the window.
3. Delete that entry from hash map as we dont want it in the window.

"""

from collections import defaultdict

def longest_sub_string(arr, k):
    count = 0

    for i in range(len(arr)):
        lookup = set()
        tmp_count = 0  
        for j in range(i, len(arr)):
            if arr[j] not in lookup:
                if len(lookup) < k:
                    lookup.add(arr[j])
                    tmp_count += 1 
                else:
                    break
            else:
                tmp_count += 1
        if len(lookup) == k:
            count = max(count, tmp_count)
    
    return count

def longest_sub_string_opt(arr, k):

    lookup = defaultdict(int)
    max_length = 0
    window_start = 0

    for window_end in range(len(arr)):

        lookup[arr[window_end]] += 1

        while len(lookup) > k:

            max_length = max(max_length, window_end - window_start)
            left_most_char_count = lookup[arr[window_start]]
            del lookup[arr[window_start]]
            window_start += left_most_char_count
    
    return max_length


assert 2 == longest_sub_string("aabbcc", 1)
assert 6 == longest_sub_string("aabbcc", 3)
assert 0 == longest_sub_string("aaabbb", 3)
assert 4 == longest_sub_string("araaci", 2)
assert 2 == longest_sub_string("araaci", 1)
assert 5 == longest_sub_string("cbbebi", 3)



            