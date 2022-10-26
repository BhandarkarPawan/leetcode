from collections import Counter 
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        start = 0 
        counts = Counter(t)
        matched = 0 

        minSubStr = ""
        minLen = float("inf")

        for end in range(len(s)):
            if s[end] in counts: 
                counts[s[end]] -= 1
                if counts[s[end]] == 0:
                    matched += 1 
                
            while matched == len(counts):
                if (end - start + 1) < minLen:
                    minLen = end - start + 1
                    minSubStr = s[start: end+1]
                if s[start] in counts:  
                    if counts[s[start]] == 0:
                        matched -= 1
                    counts[s[start]] += 1 
                start += 1
                    
        return minSubStr
            
