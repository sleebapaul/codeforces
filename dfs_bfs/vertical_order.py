"""

Leetcode 987. Vertical Order Traversal of a Binary Tree

Idea: Index the tree nodes 

                (0,0)
        (1, -1)        (1,1)

This is an important question for me and it is a "hard" problem in Leetcode.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
from typing import Optional, List

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            
            queue = [(0, 0, root.val, root)]
            
            lookup = defaultdict(list)
            
            
            while queue:
                
                level_len = len(queue)
                current_level = []
                
                for i in range(level_len):
                    x, y, val, current = queue[i]
                    
                    lookup[y].append(val)
                    
                    if current.left:
                        current_level.append((x+1, y-1, current.left.val, current.left))
                    if current.right:
                        current_level.append((x+1, y+1, current.right.val, current.right))
                        
                queue = sorted(current_level, key=lambda tup: (tup[0],tup[1], tup[2]))
                            
            
            result = []
            
            for key in sorted(lookup):
                result.append(lookup[key])
            
            return result 
        
        res = bfs(root)
        return res 
                    
                
        
        
        