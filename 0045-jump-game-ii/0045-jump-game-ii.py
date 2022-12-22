class Solution:
    def jump(self, nums: List[int]) -> int:
        
        farthest = 0 
        left = 0 
        right = 0 
        res = 0 

        while right < len(nums)-1:
            for i in range(left, right+1):
                farthest = max(farthest, nums[i] + i)
            left = right + 1 
            right = farthest
            res+=1 


        return res 