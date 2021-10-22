"""
Leetcode 199 : Binary tree right side view

Here the first idea that came to my mind was traverse to right of the tree, if no right node, take left node and go on. 
This should give the right most path in the tree.

But this is not enough. If there are paths that has more edges than right most path, that will be seen from right view as well.
So we need to start with right most path and progress to left most path. While doing it, if there is any path that has more edges than right most
path, then add the extra to the right most path and update it.  

So I took the code for getting all the paths from GoG and put my logic in the end of path. The original code first gives the left most path in the tree, 
and move to right. One clever thing I've done here was, I changed the order of traversal such that, I get the right most path, first. 

"""



from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
                
        def find_all_paths(stack, root):
            
            if root is None:
                return  
            
            stack.append(root.val)
            if root.left == None and root.right == None:
                if self.result == None:
                    self.result = stack[:]
                else:
                    if len(stack) > len(self.result):
                        tmp = stack[:]
                        self.result += tmp[len(self.result):]
            find_all_paths(stack, root.right)
            find_all_paths(stack, root.left)
            stack.pop()
            return 
            
        if root is None:
            return []
        
        self.result = None
        stack = []
        find_all_paths(stack, root)
       
        return self.result