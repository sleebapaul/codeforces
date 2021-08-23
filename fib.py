"""
Fibonacci with memoization
"""
def fib(n, memo):
    """
    TC: O(n)
    SC: O(n)

    """
    if n in memo: return memo[n]
    if n <= 2: return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    print("here", memo)
    return memo[n]

"""
Grid travel using memoization (Movement right and down)
"""

def dfs(m, n, memo):
    """
    
    TC: O(nm)
    SC: O(mn)
    
    """
    if (m,n) in memo: return memo[(m,n)]
    if m==0 or n==0: return 0
    if m==1 and n==1: return 1

    memo[(m,n)] = dfs(m-1, n, memo) + dfs(m, n-1, memo)
    return memo[(m,n)]


memo = {}
val = dfs(3, 3, memo)
print(val)