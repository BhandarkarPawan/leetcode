from collections import deque, defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = defaultdict(lambda: [])
        visited = set()
        
        queue = deque()
        queue.append(source) 

        for s, d in edges: 
            adj[s].append(d)
            adj[d].append(s)
        
        while queue: 
            curLevel = []
            for _ in range(len(queue)):
                popped = queue.popleft()
                if popped == destination:
                    return True
                if popped in visited: 
                    continue
                visited.add(popped)
                curLevel.extend(adj[popped])
            queue.extend(curLevel)
        
        return False 
        
                

            