from collections import Counter 
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 

        counts = Counter(hand)
        res = []
        
        curMin = min(hand)
        while len(res) < len(hand):
            if len(res) % groupSize == 0: 
                curMin = min(counts)

            if curMin not in counts: 
                return False 
            
            res.append(curMin)
            counts[curMin] -= 1
            
            if counts[curMin] == 0:
                del counts[curMin]

            curMin += 1 

        
        return True 
            

                
            
            
            
        
