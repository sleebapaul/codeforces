"""
Leetcode 365. Water and Jug Problem

It can be done using BFS. But really tricky. Got the idea from Leetcode discussion. 

Watch Die Hard Scene to understand the problem : https://www.youtube.com/watch?v=BVtQNK_ZUJg

To do BFS we need a graph/tree. What is that gonna be? That's the hardest part in the problem. 

To understand the tree, we should look into the first step of the Jars and Water levels 

Eg. Jar of 3 litres and 5 litres. Whats the first step? 

State 1 - Add 3 litres 
State 2 - Remove 3 litres  -> Results in negative values which makes no sense. 

State 3 - Add 5 litres 
State 4 - Remove 5 litres  -> Results in negative values which makes no sense. 

Also any state > Total available jug capacity is also not worth pursuing. 
Any visited state is also not worth pursuing as it goes in circles.


So 3 conditions. 

1. If negative state - Don't pursue
2. If state greater than target - Don't pursue 
3. If state has occured early - Don't pursue


At each step, so we have 4 four choices. Cool. Considering the conditions, the graph gonna be.

                        0
            3                       5           # -3, -5 are not pursued
        6       8               2               # 0, -2, 8, 10, 0 are not pursued 
    1                       7                   # 9, 3, 11, 3, -1, -3 are not pursued 
4                                               # We have our target       


"""

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        queue = [0]
        visited = {0}
        
        while queue:
            current = queue.pop(0)
            
            for step in [jug1Capacity, -1*jug1Capacity, jug2Capacity, -1*jug2Capacity]:
                
                next_step = current + step
                
                if next_step == targetCapacity:
                    return True
                
                if next_step > jug1Capacity + jug2Capacity or next_step < 0 or next_step in visited:
                    continue
                else:
                    visited.add(next_step)
                    queue.append(next_step)
                    
        return False


