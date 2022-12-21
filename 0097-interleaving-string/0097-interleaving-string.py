class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:        
        dp = {}

        if len(s1) + len(s2) != len(s3):
            return False 
        
        def backtrack(i, j, k):
            if k == len(s3):
                return True
            if (i, j, k) in dp: 
                return False 
            if i < len(s1) and s1[i] == s3[k] and backtrack(i+1, j, k+1):
                return True 
            if j < len(s2) and s2[j] == s3[k] and backtrack(i, j+1, k+1):
                return True 
                    
            dp[(i, j, k)] = False 
            return False 
        
        return backtrack(0,0,0)
            
                
                
                
                
                
             