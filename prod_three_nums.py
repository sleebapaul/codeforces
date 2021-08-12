"""
1294C
"""

def inp():
    """
    For taking integer inputs.
    """
    return(int(input()))

def get_n_ints(n):
    """
    For taking List inputs.
    """
    result = []
    i = 0
    while i < n:
        val = input().rstrip("\n")
        result.append(int(val))
        i += 1
    return result

def problem(number):
    seen = list()
    i = 2
    while i*i <= number:
        if i not in seen:
            if number%i == 0:
                seen.append(i)
                number = number//i

        if len(seen) == 2 and number > seen[-1]:
            seen.append(number)
            print("YES")
            print(*(seen))
            return
        i += 1

    print("NO")




n = inp()
arr = get_n_ints(n)
for i in range(n):
    problem(arr[i])