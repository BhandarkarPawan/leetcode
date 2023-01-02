class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        og = n 
        allowedDigits = [0, 1, 6, 9, 8]
        res = []
        while n > 0: 
            rem = n % 10
            if rem not in allowedDigits:
                return False
            n = n // 10
            
            if rem == 6:
                rem = 9 
            elif rem == 9:
                rem = 6
            res.append(str(rem))
        
        print(res)
        if not res:
            return False 
        
        if int("".join(res)) == og:
            return False 
            
        return True 