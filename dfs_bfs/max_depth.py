"""
Leetcode 104. Maximum Depth of Binary Tree

My Idea: This is essentially calculation og height of the binary tree. 

But in height, we count the number of edges but here, we need to count the nodes. 
So, base case returns 0 (No of edges = No of nodes - 1)

Other case would be selecting the maximum depth between left arm or right arm of the node.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root is None:
                return 0
            else:
                return 1+ max(dfs(root.left), dfs(root.right))
        
        max_depth = dfs(root)
        return max_depth
                
