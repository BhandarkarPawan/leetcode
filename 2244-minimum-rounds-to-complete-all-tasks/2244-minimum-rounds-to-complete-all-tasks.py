from collections import Counter 

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        counts = Counter(tasks)
        res = 0 
        
        for k, v in counts.items():    
            print(k, v)
            if v % 3 == 0:
                res += v // 3 
            elif v % 3 == 2: 
                res += (v // 3) + 1 
            elif v % 3 == 1:
                if v < 3:
                    return -1  
                res += (v // 3) + 1 
        
        return res 
            
            
            