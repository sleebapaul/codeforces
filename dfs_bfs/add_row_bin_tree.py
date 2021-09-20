"""
Leetcode 623. Add One Row to Tree

The idea is simple. Do a BFS. Whenever, we find the tree_height equals to depth, just rearrange the nodes and stop BFS.


"""
from collections import deque 
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        
        def bfs(root, val, depth):
            
            tree_height = 1
            queue = deque()
            queue.append(root)
            
            while queue:
                level_size = len(queue)
                                
                for _ in range(level_size):
                    
                    current = queue.popleft()
                    if tree_height == depth-1:

                        left = TreeNode(val)
                        right = TreeNode(val)

                        if current.left:
                            left.left = current.left
                            
                        if current.right:
                            right.right = current.right

                        current.left = left
                        current.right = right
                        
                    else:
                        if current.left:
                            queue.append(current.left)
                        if current.right:
                            queue.append(current.right)
                                  
                tree_height += 1 
                
        if depth == 1:
            node = TreeNode(val)    
            node.left = root
            return node 
        
        bfs(root, val, depth)
        return root 

