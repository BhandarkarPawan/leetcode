from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])


        queue = deque()
        visited = set()

        num_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    num_oranges +=1 
                if grid[i][j] == 2: 
                    queue.append((i,j))
                    visited.add((i,j))
        
        if not queue:
            if num_oranges > 0:
                return -1 
            return 0

        mins = 0 
        while queue:
            mins += 1 
            nextLevel = [] 
            for _ in range(len(queue)):
                i, j = queue.popleft()

                neighbors = [
                    (i+1, j),
                    (i-1, j),
                    (i, j+1),
                    (i, j-1)
                ]

                for a, b in neighbors: 
                    if a >= 0 and b >= 0 and a <m and b <n and (a,b) not in visited: 
                        if grid[a][b] == 1:
                            visited.add((a,b))
                            nextLevel.append((a,b))
            
            queue.extend(nextLevel)
        
        if len(visited) == num_oranges:
            return mins - 1 
        
        return -1 
        




                
