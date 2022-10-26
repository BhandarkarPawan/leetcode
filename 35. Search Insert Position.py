# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)

        while (start < end):
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                # earliest possible position is after mid
                start = mid + 1
            else:
                # earliest possible position is either at current index or before
                end = mid

        return start
