"""
Leetcode 101 Symmetric Tree

Check the picture https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg

My idea: 

    2               2
3       4       4       3

These are symmetric. Which means, we need to do the same stuff as same tree (Leetcode 100) but with some traversal trick. 

Here the comparison is between left child and right child of the mirror node. 

Say you are at mirror node 2, the comparison is between 3 (left of first 2) and 4 (right of second 2)
Then, the opposite. 

traverse(root1.left, root2.right)
traverse(root1.right, root2.left)

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
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
            
            traverse(root1.left, root2.right)
            traverse(root1.right, root2.left)
        
        traverse(root.left, root.right)
        return self.result