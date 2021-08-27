"""
4C
"""

def inp():
    """
    For taking integer inputs.
    """
    return(int(input()))

def get_n_strings(n):
    """
    For taking List inputs.
    """
    result = []
    i = 0
    while i < n:
        val = input().rstrip("\n")
        result.append(str(val))
        i += 1
    return result


def problem(n, arr):

    seen = {}
    for i in range(n):
        if arr[i] not in seen:
            print("OK")
            seen[arr[i]] = 1
        else:
            num_to_add = seen[arr[i]]
            print(arr[i]+str(num_to_add))
            seen[arr[i]] += 1

n = inp()
my_input = get_n_strings(n)

problem(n, my_input)

