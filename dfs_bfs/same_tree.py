"""
100. Same Tree

Check if both the binary trees are the same. 

My idea: Traverse the same way through both trees, lets see if the conditions break anywhere

Conditions 

1. The nodes should not be None individually. If None, both are None. 
2. If nodes, the values should be the same for same node. 

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.result = True
        
        def traverse(root1, root2):
            
            if root1 is None and root2:
                self.result = False
                return
            
            if root1 and root2 is None:
                self.result = False
                return 
            
            if root1 is None and root2 is None:
                return 
            
            if root1.val != root2.val:
                self.result = False
                return
            
            traverse(root1.left, root2.left)
            traverse(root1.right, root2.right)
            
        
        traverse(p, q)
        
        return self.result