"""
327A

Kedane's Algorithm - Signals

1. Based on a subarray operation
2. Maximize/Minimize something
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


def problem(arr):
    num_of_ones = 0
    cost = []
    for i in range(len(arr)):
        if arr[i]:
            cost.append(-1)
            num_of_ones += 1
        else:
            cost.append(1)

    if num_of_ones == len(arr):
        print(num_of_ones - 1)
        return

    max_score = 0
    tmp_score = 0
    for i in range(len(cost)):
        tmp_score = max(0, tmp_score + cost[i])
        max_score = max(max_score, tmp_score)

    print(max_score + num_of_ones)


n = inp()
arr = invr()
problem(arr)
