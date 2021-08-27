"""
Vanya and Lanterns
492B
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
    return(list(map(int,input().split())))


def problem(n, l, lanterns):

    sorted_lanterns = sorted(lanterns) # [0, 3, 5, 7, 9, 14, 15]

    dist = 0
    dist_start = 0
    dist_end = 0
    if sorted_lanterns[0] != 0:
        dist_start = sorted_lanterns[0]

    if sorted_lanterns[-1] != l:
        dist_end = l - sorted_lanterns[-1]

    dist = max(dist_end, dist_start)

    for i in range(1, len(sorted_lanterns)):
        dist = max(dist, 0.5 * (sorted_lanterns[i]-sorted_lanterns[i-1])) # max(2, 14-9) => 2

    print("{:.10f}".format(float(dist)))


line = invr()
n = line[0]
l = line[1]

lanterns = invr()

problem(n , l , lanterns)
