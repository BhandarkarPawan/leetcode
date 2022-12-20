from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        adj = { i : rooms[i] for i in range(len(rooms))}

        queue = deque(adj[0])
        del adj[0]

        while queue: 
            curLevel = []
            for _ in range(len(queue)):
                popped = queue.popleft()
                if popped not in adj: 
                    # We have previously visited it 
                    continue
                curLevel.extend(adj[popped])
                del adj[popped]
            queue.extend(curLevel)
        
        return len(adj) == 0 


            