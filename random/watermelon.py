import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    """
    For taking integer inputs.
    """
    return(int(input()))
def inlt():
    """
    For taking List inputs.
    """
    return(list(map(int,input().split())))
def insr():
    """
    For taking string inputs.
    """
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    """
    For taking space seperated integer variable inputs.
    """
    return(map(int,input().split()))

def watermelon(w):

    i = 2
    while i <= w//2:
        pete = i
        bill = w - i
        if pete%2==0 and bill%2==0:
            print("YES")
            return
        i += 1
    print("NO")
    return

my_input = inp()
watermelon(my_input)