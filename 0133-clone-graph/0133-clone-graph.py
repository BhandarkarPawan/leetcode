"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def rec(self, visited, node: 'Node'):
        if not node:
            return 
        if node in visited:
            return visited[node]
        
        newNode = Node(node.val, [])
        visited[node] = newNode
        newNode.neighbors = [
            self.rec(visited, n) for n in node.neighbors
        ]

        return newNode

    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        
        return self.rec(visited, node)

        
