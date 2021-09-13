"""

Leetcode 112. Path Sum

DFS solution would be based on the idea of 

1. If node is None, that means the sum has passed in the previous level (Leaf level), so return False
2. If a leaf node and target - node.val = 0. which means target is met

Target is reduced each time the children are called. 

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def dfs(root, target):
            
            if root is None:
                return False
            
            if target - root.val == 0 and root.left is None and root.right is None:
                return True
            
            left = dfs(root.left, target - root.val)
            right = dfs(root.right, target - root.val)
            
            return left or right
        
        res = dfs(root, targetSum)
        return res 
        