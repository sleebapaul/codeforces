"""

Find maximum (or minimum) sum of a subarray of size K

https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/


"""

# brute force 
def max_k_subarray(array, k):

    max_sum = float("-inf")

    for i in range(len(array)-k):
        max_sum = max(max_sum, sum(array[i:i+k]))
    
    return max_sum


# optimized using sliding window 
# add the new element to sliding window and remove the left most in the window
# keep track of sum

def max_k_subarray_opt(array, k):
    window_sum = 0
    first_element_idx = 0  
    max_sum = float("-inf")

    for i in range(len(array)):

        window_sum += array[i]

        if i >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= array[first_element_idx]
            first_element_idx += 1

    return max_sum



arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

assert 39 == max_k_subarray(arr, k)
assert 39 == max_k_subarray_opt(arr, k)

