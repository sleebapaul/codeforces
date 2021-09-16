"""
Leetcode 437. Path Sum III

Idea: Not just at leaf nodes, at each node go through the stack, find if there is a sub sum which is equals to target. 
The sub sum calculation can be done in linear time, as in the question, it is givent that, 

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

"""


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, stack, targetSum):
            
            if root is None:
                return 
            
            stack.append(root.val)
            
            tmp_sum = sum(stack)
            i = 0
            
            while i < len(stack):
                if tmp_sum == targetSum:
                    self.path_count += 1
                tmp_sum -= stack[i]
                i+=1
                
            dfs(root.left, stack, targetSum)
            dfs(root.right, stack, targetSum)
            
            stack.pop()
        
        self.path_count = 0
        dfs(root, [], targetSum)
        
        return self.path_count

        