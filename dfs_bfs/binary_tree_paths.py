"""
257. Binary Tree Paths

The approach stays with the Leetcode 993 Cousin nodes

Same logic can be used for searching a node and get the path. Change will be on the base condition. 

Here it is checking the node. There it will be checking if the target of the search.

"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(root):
            
            if root is None:
                return 
            
            self.path.append(root.val)
            
            if root.left is None and root.right is None:
                tmp = "->".join([str(x) for x in self.path])
                self.output.append(tmp)
            
            dfs(root.left)
            dfs(root.right)
            
            self.path.pop()
        
        
        self.path = []
        self.output = []
        
        dfs(root)
        
        return self.output
        