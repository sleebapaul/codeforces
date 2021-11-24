"""
1861. Rotating the Box

This is question which employs both matrix 90 degree rotation and two pointer

Rotation can be done easily with zip command.

Idea is to bring all the "#" to right side, considering the block "*". 

[["*","#","*",".",".",".","#",".","*","."]]

So we start from right to left. 

If the matrix[position] == "*", that is a reset. Because, it will hold the rest from that position.
So the move_index = position - 1

If the matrix[position] == "#", do the swap and move_index -= 1.
Since we have already covered the "*", obviously the possibility of swap is either with two "#" or a "#" and a "." 


"""

from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        rows = len(box)
        
        for row in range(rows):
            move_index = len(box[row]) - 1 
            position = len(box[row]) - 1  
            
            while position >= 0:
                if box[row][position] == "*":
                    move_index = position - 1
                
                elif box[row][position] == "#":
                    box[row][move_index], box[row][position] = box[row][position], box[row][move_index]
                    move_index -= 1
                
                position -= 1 

        return zip(*box[::-1])