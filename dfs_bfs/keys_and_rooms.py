"""
Leetcode 841. Keys and Rooms

Typical dfs/bfs problem 


"""

from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        def build_graph(rooms):
            graph = {}
            
            for i, room in enumerate(rooms):
                graph[i] = room
            return graph 
        
        def bfs(graph, visited):
            queue = [0]
            
            while queue:
                current = queue.pop(0)
                if current in visited:
                    continue
                else:
                    visited.add(current)
                    for child in graph[current]:
                        if child != current:
                            queue.append(child)
                            
        
        graph = build_graph(rooms) 
        
        visited = set()
        
        bfs(graph, visited)
        
        if len(visited) == len(rooms):
            return True
        
        return False
            
        