"""

Leetcode 124. Binary Tree Maximum Path Sum

Very well explained here: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

But the basic idea comes from Leetcode 543 
 
"""


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float("-inf")
        
        def dfs(root):
            
            if root is None:
                return 0
                        
            left_sum  = max(0, dfs(root.left))
            right_sum = max(0, dfs(root.right))
            
            self.max_sum = max(self.max_sum, root.val + left_sum + right_sum)
                        
            return max(left_sum, right_sum) + root.val
            
        dfs(root)
        
        return self.max_sum 