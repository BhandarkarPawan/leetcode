from heapq import * 
from collections import defaultdict 
from collections import deque 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        
        edges = defaultdict(list)
        for u, v, w in times: 
            edges[u].append((v, w))

        minheap = [(0, k)] 
        visited = set() 
        t = 0 
        
        while minheap: 
            w1, n1 = heappop(minheap)
            if n1 in visited: continue 
            
            visited.add(n1)
            t = max(t, w1)
            
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heappush(minheap, (w2 + w1, n2))
            
        if len(visited) == n:
            return t 
        
        return -1 