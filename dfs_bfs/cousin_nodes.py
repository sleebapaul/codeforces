"""

993. Cousins in Binary Tree

Idea is simple. Find the paths of x node and y node. Check if they are equal length (same level) and their parents are different

This code can be used for printing all the paths, as well as finding the path from node A to node B. 

If printing all paths, the base case changes to check if leaf
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def search(root, node, path):
            
            if root is None:
                return False
            
            path.append(root.val)
            
            if root.val == node:
                return True
            
            if (search(root.left, node, path)) or (search(root.right, node, path)):
                return True
            
            path.pop()
            return False 
        
        # Corner cases 

        if x == y:
            return True
        
        if root is None:
            return False
            
        path_x = []
        path_y = []
        search(root, x, path_x)
        search(root, y, path_y)
                
        if len(path_x) == len(path_y):
            if path_x[-2] != path_y[-2]:
                return True
        return False
            
                