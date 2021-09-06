"""
Leetcode 404. Sum of Left Leaves

My idea was to track the left nodes and find the leaf nodes from them. Didn't work out. But simple approach would be, 

when we call root.left, we it is gonna be a left node at the output. If it is a node with not left or right child, it is a left leaf

So using that logic, things are more straight forward. Just pass an indicator that, it was a left node call. 


"""


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, is_left):
            
            if not root:
                return None
            if root.left is None and root.right is None and is_left:
                result[0] += root.val
            
            dfs(root.left, True)
            dfs(root.right, False)
            

        result = [0]
        dfs(root, False)
        return result[0]