"""
Leetcode 617. Merge Two Binary Trees

My idea : Traverse alike through the two trees, if both roots available, return the sum else available value. 

But got stuck on, what happens when both nodes are None. 

Here the solution is inspired from the Leetcode discussion. 

If root1 is None use root2 and vice versa. This will take care of the case of both roots are None

If both are available, create a TreeNode. find the sum. Now explore the left and right paths of the node
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
       
        def dfs(root1, root2):
            
            if root1 is None:
                return root2
            elif root2 is None:
                return root1
          
            new_root = TreeNode()
            new_root.val = root1.val + root2.val 

            new_root.left = dfs(root1.left, root2.left)
            new_root.right = dfs(root1.right, root2.right)
            
            return new_root
        
        
        new_root = dfs(root1, root2)
        
        return new_root
                