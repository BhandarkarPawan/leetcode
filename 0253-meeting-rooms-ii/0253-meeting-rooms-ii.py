from heapq import * 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        res = 0 
        minheap = []
        for start, end in intervals: 

            if minheap and minheap[0][0] <= start: 
                heappop(minheap)
            else: 
                res += 1 
                
            heappush(minheap, (end, start))
        
        return res 
            
        