"""
Leetcode 116. Populating Next Right Pointers in Each Node

Idea is simple. Do a BFS. Collect the nodes in each level. Add them into a queue. 

Now, pop each time, and assign the .next variable accordingly

"""
# Definition for a Node.

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def bfs(root):
            queue = deque()
            queue.append(root)
            result = []
            
            while queue:
                level_size = len(queue)
                current_level = deque()
                
                for i in range(level_size):
                    current_node = queue.popleft()
                    current_level.append(current_node)
                    
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                
                while current_level:
                    _current = current_level.popleft()
                    if current_level:
                        _current.next = current_level[0]
                    else:
                        _current.next = None 
        
        if root is None:
            return root
        
        bfs(root)
        
        return root
                        
                    
            
            