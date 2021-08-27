"""
Codeforces
1371 C

It is a very simple logic.

1 If no. of cookies < no. of people coming, then we cannot serve everyone. 

Now let's talk about the type of people coming. 

2. Type A people: Selects the type of cookie that is abundant, if not available, they take the other one. 
    - If vanilla is abundant, they take vanilla. If chocolate is abundant, they take chocolate. 
3. Type B people: Selects the type of cookies that is least available. 

If we can satisfy, the Type B people, provided first condition is satisfied, we can serve Type A people. 

Eg. Vanilla = 7, Chocolate = 5, Type A = 8, Type B = 4

Type B comes in and eat the minority cookie, i.e. Chocolate => (7, 1) <=> (8, 0)
Type A comes in and eat the majority cookie, i.e. Vanilla => (0, 1) <=> (1, 0) 
Type a comes in and eat the majority cookie, i.e. Chocolate => (0, 0) <=> (0, 0)

So the minority cookie type should have enough number to feed Type B people. 

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


def problem(vanilla, chocolate, type_a, type_b):

    if vanilla + chocolate < type_a + type_b:
        print("No")
        return

    if min(vanilla, chocolate) < type_b:
        print("No")
        return 
        
    print("Yes")

n = inp()

for _ in range(n):
    [van, choc, van_pep, choc_pep] = invr()
    problem(van, choc, van_pep, choc_pep)