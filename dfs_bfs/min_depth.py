"""
Leetcode 111. Minimum Depth of Binary Tree

Here things are bit complicated than max depth. 

In a root with atleast one right and left, the max depth logic will work. 

But consider the case. 

2
    3
        4
            5

    2
3       4
            5
                6

My idea: the actual base case is not node is None. The correct one is, root.left and root.right are None, then thats the leaf node.
So base cases changes accordingly.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root.left is None and root.right is None:
                return 1
            elif root.left is None:
                return 1 + dfs(root.right)
            elif root.right is None:
                return 1 + dfs(root.left)
            else:
                return 1 + min(dfs(root.left), dfs(root.right))
            
        if root is None:
            return 0
        
        min_depth = dfs(root)
        return min_depth