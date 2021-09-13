"""
Leetcode 113. Path Sum II

Logic using a stack. 

The code is used to find all the paths in a tree. We can use this code for many problems related to paths. 

A stack is used to keep track of the paths. Once the children as visited, the parent is removed from the stack. 
That means, going one node up in the tree to restart the other part of the tree. 



"""

from typing import Optional, List
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.paths = []
        
        def dfs(root, stack, target):
            
            if root is None:
                return 
            
            stack.append(root.val)
            
            if root.left is None and root.right is None:
                if sum(stack) == target:
                    self.paths.append(stack[:])
            
            if root.left:
                dfs(root.left, stack, target)
            
            if root.right:
                dfs(root.right, stack, target)
            
            stack.pop()
        
        dfs(root, [], targetSum)
        
        return self.paths
        
            
            
            
        