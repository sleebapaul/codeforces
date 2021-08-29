"""
Leetcode 
226. Invert Binary Tree

Look at the image: https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg

It is quite straight forward.
My idea: Go to each root, do a swap of right and left child 

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse(root):
            if root:
                tmp = root.left
                root.left = root.right
                root.right = tmp
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)
        return root