"""
129. Sum Root to Leaf Numbers

My idea: Get all paths. Create the leaf number. Add to sums.

So when it is a leaf node, 

if root.left is None and root.right is None:
    tmp = stack[:]
    i = 1
    sum_num = 0
    while tmp:
        val = tmp.pop()
        sum_num += i * val
    self.path_num_sums += sum_num 


But the better idea is whenever we call DFS on left and right node,
1. Consider the parent and child (left or right)
2. Which means it is a two digit number 

            4
        9       0
    5       1

Consider the path 4->9->5. Now consider the node 4, 9. 

If we consider only these two, it is a 2 digit number with 4 * 10 + 9 

Now consider, 49 amd 5 -> 49*10 + 5

So we get the sum eventually. 4 * 100 + 9 * 10 + 5 => (4 * 10 + 9)* 10 + 5
    
"""

# Definition for a binary tree node.

from typing  import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.path_sum_nums = 0
        
        def dfs(root, stack):
            
            if root is None:
                return 
            
            stack.append(root.val)
            
            if root.right is None and root.left is None:
                self.path_sum_nums += stack[-1]
            
            if root.left:
                root.left.val += root.val * 10
                dfs(root.left, stack)
            
            if root.right:
                root.right.val += root.val * 10
                dfs(root.right, stack)
            
            stack.pop()
        
        dfs(root, [])
        return self.path_sum_nums
                
                    
        