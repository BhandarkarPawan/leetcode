class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        
        lastIndex = {
            s[i]: i for i in range(len(s))
        }

        res = []
        start = 0
        end = 0 
        prevend = -1 
        
        while end < len(s)-1:
            end = lastIndex[s[start]]
            while start < end: 
                end = max(end, lastIndex[s[start]])
                start += 1 
            res.append(end-prevend)
            prevend = end 
            start = end + 1 
        
        return res 
