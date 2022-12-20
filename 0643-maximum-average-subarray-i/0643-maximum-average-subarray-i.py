class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        curSum = maxSum 
        
        start = 0 
        for end in range(k, len(nums)):
            curSum = curSum - nums[start] + nums[end]
            maxSum = max(curSum, maxSum)
            start += 1 
        
        return maxSum / k 
        
        
        
        
        
        