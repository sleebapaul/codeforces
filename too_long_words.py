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


def long_words(n, words):

    for i in range(n):
        word = words[i]
        if len(word) > 10:
            first_letter = word[0]
            last_letter = word[-1]
            print(first_letter + str(len(word)-2) + last_letter)
        else:
            print(word)
    return

n = inp()
my_input = get_n_strings(n)
long_words(n, my_input)