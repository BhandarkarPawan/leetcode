# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
    
        def swap(left, right):
            while left < right: 
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1

        swap(0, n-1)
        swap(0, k-1)
        swap(k, n-1)
        
        

            
            