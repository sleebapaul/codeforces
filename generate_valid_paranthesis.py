"""
22. Generate Parentheses

This is a brilliant case of recursion.  And it is not my solution. 

Idea: 

1. If "(" used are less than available, then use "("

2. If ")" used are less than no. of "(", use ")" 

3. When it reaches twice the n -> collect it 

- First travel

( -> ( -> ( -> ) -> ) -> ) 

- Second travel 

If will recurse and return upto => "(("

( -> ( -> now close < open so ----> ) 

( -> ( -> ) -> ( -> ) -> ) 

- Third travel 

Recurse upto => "(()" 

( -> ( -> ) Again close < open------> ) 

( -> ( -> ) -> ) -> ( -> ) 

And go on. Dance of recursion.

Use https://pythontutor.com/visualize.html#mode=display for visualizing the beautiful algorithm.

"""

from typing import List

class Solution:
    
    def dfs(self, n, _open, _close, _current,  result):
        
        if len(_current) == 2*n:
            result.append(_current)
            return
        
        if _open < n:
            self.dfs(n, _open+1, _close, _current+"(", result)
            
        if _close < _open:
            self.dfs(n, _open, _close+1, _current+")", result)
        
        return 
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 0:
            return []
        
        if n == 1:
            return ["()"]
        
        result = []
        
        self.dfs(n, 0, 0, "", result)
        
        return result
        
        
