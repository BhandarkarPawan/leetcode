from collections import deque 
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        colors = [-1] * (n + 1)
        adj = {} 
        
        for i in range(1, n+1):
            adj[i] = []
        
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
         
        for i in range(1, n+1):
            if colors[i] == -1: 
                queue = deque([i])
                colors[i] = 0
                while queue: 
                    popped = queue.popleft()
                    for n in adj[popped]:
                        if colors[n] == colors[popped]:
                            return False
                        if colors[n] == -1:
                            colors[n] =  1 - colors[popped]
                            queue.append(n)
        return True 


