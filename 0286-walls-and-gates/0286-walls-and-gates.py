class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647

        m  = len(rooms)
        n = len(rooms[0])

        def findConnected(i, j, visited):
            neighbors = [
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1)
            ]

            for a, b in neighbors: 
                if (
                    a >= 0 and b >=0 and 
                    a < m and b < n and 
                    (a,b) not in visited and 
                    rooms[a][b] != -1 and 
                    rooms[a][b] != 0 and 
                    rooms[a][b] > rooms[i][j] + 1
                ):
                    visited.add((a,b))
                    rooms[a][b] = rooms[i][j] + 1
                    findConnected(a, b, visited)
                    visited.remove((a,b))

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    visited = set()
                    visited.add((i, j))
                    findConnected(i, j, visited)



