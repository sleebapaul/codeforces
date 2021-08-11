"""
Kedane's algorithm
"""

def inp():
    """
    For taking integer inputs.
    """
    return(int(input()))


def invr():
    """
    For taking space seperated integer variable inputs.
    """
    return(list(map(int, input().split())))


def problem(n, arr):
    result = 0
    tmp = 0

    for i in range(n):
        tmp = max(0, tmp+arr[i])
        result = max(result, tmp)
    if result == 0:
        print(max(arr))
    else:
        print(result)

n = inp()
arr = invr()
problem(n, arr)
