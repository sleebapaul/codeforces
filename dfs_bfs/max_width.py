"""
Leetcode 662 Maximum Width of Binary Tree

My idea was to solve the problem using BFS. But I was not able to fulfill all the test cases.

The right way to do it, is indexing each node. E.g.

                1
        3               2
    5       3               9

When we index it, we will get root as 0

                0
        0               1
    0       1       2       3

To get this, the general formula is 

for left node: 2*i where i is the ith node in a level
for right node: 2*i+1 where i is the ith node in a level

Now do the BFS by adding index. 


"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = [[root, 0]]
        result = 0

        while queue:                 
            tmp = []
            for i in range(len(queue)):
                node, idx = queue.pop(0)
                tmp.append(idx)
                if node.left:
                    queue.append([node.left, 2*idx])
                if node.right:
                    queue.append([node.right, 2*idx+1])
            print(tmp)
            result = max(result, 1+(tmp[-1] - tmp[0]))
        return result
    