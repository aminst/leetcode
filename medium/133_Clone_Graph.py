"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None
        visited = dict()
        def dfs(node):
            if node.val in visited:
                return visited[node.val]
            new_node = Node(node.val, None)
            visited[node.val] = new_node
            for i, neighbor in enumerate(node.neighbors):
                if i == 0:
                    new_node.neighbors = []

                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)
            return new_node
        
        return dfs(node)
