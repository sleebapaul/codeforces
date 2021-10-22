"""
Leetcode 513. Find Bottom Left Tree Value

Finding the left most value is last row is pretty straight forward.

Do BFS. Stop on last level. Get the first element 

It is a useful pattern in BFS problems. Keeping track of next_level and current_level

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            
            current_level = [root]
            
            while current_level:
                next_level = []
                
                for i in range(len(current_level)):

                    if current_level[i].left:
                        next_level.append(current_level[i].left)
                    if current_level[i].right:
                        next_level.append(current_level[i].right)
                
                if next_level == []:
                    return current_level[0].val
                current_level = next_level
            return next_level[0].val
        
        value = bfs(root)
        return value