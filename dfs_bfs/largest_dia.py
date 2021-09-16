"""
543. Diameter of Binary Tree

It is a very simple idea actually. First write the code to calculate the height.

Now take a step back. What is height of a binary tree? It is the largest number of edges present among the left travel and right travel of a node.
Usually we do it only for the root node as height of the tree is defined like that. But here, we need the largest path that can pass or not pass through the root.

But one thing is for sure. The path should have some parent node, through which this longest path goes through. 

Now connect the dots. 

We get left height and right height for each node to find the height of the tree. If we can update a variable every time we get a left height and right height, 
then at that parent node mention above, we'll get the maximum length aka diameter 

"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_len = 0
        
        def dfs(root):
            if root is None:
                return 0
            
            left_count = dfs(root.left)
            right_count = dfs(root.right)  
            
            # When left count and right count are calculated for each node, check if the sum of these counts are greater than current max_len
            self.max_len = max(self.max_len, left_count + right_count)
            
            return 1 + max(left_count, right_count)
        
        dfs(root)
        
        return self.max_len
        