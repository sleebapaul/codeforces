"""
"""


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

def inp():
    """
    For taking integer inputs.
    """
    return(int(input()))


def teams(n, problems):
    result = 0
    for i in range(n):
        problem = problems[i]
        count = 0
        for char in problem:
            if ord(char) == 49:
                count += 1
        if count >= 2:
            result += 1
    print(result)

n = inp()
my_input = get_n_strings(n)
teams(n, my_input)
