"""
130. Surrounded Regions
Leetcode

Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.

Idea: 

So what this means is, we need to understand the "O" that are neighbours of "O" in the edges. So we do the dfs on only those "O"s that are present in the edges.
If we find neigbouring "O"s of the edge "O"s, those can't be flipped as well. 

So we mark all these positions with a temperory variable "T". 

I've struggled to find out this notion of the problem. 
I've been trying to do the search of each "O" and find edgy "O". Exactly reverse. 
Got this idea from Leetcode discussion.

"""

from typing import List

class Solution:
    def solve(self, matrix: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        def dfs(matrix, i, j):
            
            if i > nrows-1 or i < 0 or j < 0 or j > ncols-1 or matrix[i][j] != "O":
                return 
            matrix[i][j] = "T"
            dfs(matrix, i+1, j, )
            dfs(matrix, i-1, j, )
            dfs(matrix, i, j+1, )
            dfs(matrix, i, j-1, )

        for i in range(nrows):
            for j in range(ncols):
                if i == 0 or i == nrows-1 or j == 0 or j == ncols-1:
                    if matrix[i][j] == "O":
                        dfs(matrix, i, j)

        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == "T":
                    matrix[i][j] = "O"
                else:
                    matrix[i][j] = "X"
        print(matrix)
        return 

            
soln = Solution()

test = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

soln.solve(test)