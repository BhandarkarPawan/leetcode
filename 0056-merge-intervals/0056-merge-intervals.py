from heapq import * 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        heapify(intervals)
        
        res = [] 
        while len(intervals) > 1: 
            first = heappop(intervals)
            second = heappop(intervals)
            
            if (first[1] >= second[0] and first[1] <= second[1]) or (second[1] >= first[0] and second[1] <= first[1]):
                merged = [
                    min(first[0], second[0]),
                    max(first[1], second[1])
                ]
                heappush(intervals, merged)
            else: 
                res.append(first)
                heappush(intervals, second)
            
        
        return res + intervals
                
            
            