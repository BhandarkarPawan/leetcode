class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        canFinish = [False] * n

        for i in range(n-1, -1, -1):
            if nums[i] >= n - i -1:
                canFinish[i] = True 
                continue
            for j in range(i+nums[i], i, -1):
                if canFinish[j]:
                    canFinish[i] = True 
                    continue 
        
        return canFinish[0]


            