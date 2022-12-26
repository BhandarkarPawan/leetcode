from heapq import * 

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        res = [] 

        for q in queries: 
            curSum = 0 
            run = 0 
            for n in nums: 
                if curSum + n > q: 
                    break 
                curSum += n 
                run += 1 
            
            res.append(run)
        
        return res 

