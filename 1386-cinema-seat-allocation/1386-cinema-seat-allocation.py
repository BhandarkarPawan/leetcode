from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        resMap = {
            x[0] : [True, True, True] for x in reservedSeats
        }
        
        res = 0
        
        for row, seat in reservedSeats: 
            if seat in [2, 3, 4, 5]: 
                resMap[row][0] = False 
            if seat in [4, 5, 6, 7]: 
                resMap[row][1] = False 
            if seat in [6, 7, 8, 9]: 
                resMap[row][2] = False 

        for left, center, right in resMap.values(): 
            if left and right:
                res += 2 
            elif center or left or right: 
                res += 1

        emptyRows = n - len(resMap)
        return res + emptyRows * 2 



