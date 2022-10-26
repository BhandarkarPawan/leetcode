class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start = 0
        end = 0 
        curSum = 0
        minLen = float("inf")
        
        while end < len(nums):
            curSum += nums[end]
            while curSum >= target and start < end: 
                minLen = min(minLen, end-start+1)
                curSum -= nums[start]
                start += 1 
            
            if curSum >= target: 
                minLen = min(minLen, (end-start+1))
            end += 1 
        
        if minLen == float("inf"):
            return 0 
        return minLen 
            

            