class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        diff = [x-y for x,y in zip(capacity, rocks)]
        diff.sort()
        res = 0 
        
        for d in diff: 
            if d == 0:
                res += 1 
            elif d <= additionalRocks: 
                additionalRocks -= d 
                res += 1 
        
        return res



        

