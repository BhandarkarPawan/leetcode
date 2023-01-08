from collections import Counter 
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums) % k != 0:
            return False 

        counts = Counter(nums)
        start = min(nums)
        
        res = []
        curNum = min(nums)
        
        while len(res) < len(nums):
            if len(res) % k == 0:
                curNum = min(counts)
                
            if curNum not in counts:
                return False 
            
            res.append(curNum)
            counts[curNum] -= 1 
            if counts[curNum] == 0:
                del counts[curNum]
            
            
            curNum += 1 
            
        return True  
            
            
            



        