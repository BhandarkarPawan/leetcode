from heapq import * 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))
        
        frontier = [(0,0)]
        visited = set() 
        res = 0 
        
        while len(visited) < len(points):
            dist, node = heappop(frontier)
            if node in visited: continue
            visited.add(node) 
            res += dist 

            q = points[node]
            for i, p in enumerate(points): 
                if p == q: continue
                heappush(frontier, (manhattan(p, q), i)) 
        
        return res 



