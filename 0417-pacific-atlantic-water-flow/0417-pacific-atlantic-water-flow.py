class Solution:

    

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        pacificFlow = [[0] * n for _ in range (m)]
        atlanticFlow = [[0] * n for _ in range (m)]

        pacificVisited = set()
        atlanticVisited = set()
        
        def bfs(i, j, flow, visited):
            
            neighbors = [
                (i - 1, j),
                (i + 1, j),
                (i, j + 1),
                (i, j - 1)
            ]

            for a, b in neighbors: 
                if a < m and b < n and a >= 0 and b >= 0 and (a, b) not in visited: 
                    visited.add((i,j))
                    if heights[a][b] >= heights[i][j] and flow[i][j]: 
                        flow[a][b] = True 
                        bfs(a, b, flow, visited)
       
        for j in range(n):
            pacificFlow[0][j] = True
            bfs(0, j, pacificFlow, pacificVisited)
            
            atlanticFlow[m-1][j] = True
            bfs(m-1, j, atlanticFlow, atlanticVisited)
        
        for i in range(m):
            pacificFlow[i][0] = True
            bfs(i, 0, pacificFlow, pacificVisited)
            
            atlanticFlow[i][n-1] = True
            bfs(i, n-1, atlanticFlow, atlanticVisited)

        
        res = []
        for i in range(m):
            for j in range(n):
                if pacificFlow[i][j] and atlanticFlow[i][j]:
                    res.append((i, j))
        
        return res 




                    
            
                
                    
            


         


