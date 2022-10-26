class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums
        maxSum = res[0]

        for i in range(1, len(nums)):
            res[i] = max(res[i], res[i] + res[i-1])
            maxSum = max(maxSum, res[i])

        return maxSum
