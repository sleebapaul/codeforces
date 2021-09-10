"""
Leetcode 690. Employee Importance

Idea: Do a simple DFS and keep adding the importance. Build a graph for easy indexing.

"""

from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = {}
        for employee in employees:
            graph[employee.id] = employee
        
        self.importance = 0
            
        def dfs(graph, id):
            
            self.importance += graph[id].importance
            
            if graph[id].subordinates:
                for sub in graph[id].subordinates:
                    dfs(graph, sub)
        
        dfs(graph, id)
        return self.importance
                    
            
            