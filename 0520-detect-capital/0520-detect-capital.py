class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        def isCapital(c):
            return c >= 'A' and c <= 'Z'
        
        for i in range(len(word)):
            if i > 0 and isCapital(word[i]) and not isCapital(word[i-1]):
                return False 
            if i > 1 and not isCapital(word[i]) and isCapital(word[i-1]):
                return False 
            
        return True 
                