"""
1376. Time Needed to Inform All Employees

My idea: Largest path cost. Get all the paths, calculate the path weight sum. 

Exit condition of recursive call would be, the leaf node employees don't have the subordinates. So it can be found from the managers list. 

This solution is a bit slow in Leetcode submission. More optimized way is to used DP.

"""
from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        self.path = []
        self.max_time = 0
        
        def build_graph(manager):
            
            graph = defaultdict(list)
            
            for i, j in enumerate(manager):
                if j != -1:
                    graph[j].append(i)

            return graph
        
        def dfs(graph, head, informTime):
            
            self.path.append(informTime[head])
            
            if graph[head] == []:
                if self.max_time < sum(self.path):
                    self.max_time = sum(self.path) 
            else:
                for val in graph[head]:
                    dfs(graph, val, informTime)
            
            self.path.pop()
            
        
        graph = build_graph(manager)
            
        dfs(graph, headID, informTime)
        return self.max_time
            
            
            
        