class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1 = len(nums1)
        n2 = len(nums2)

        # n1 x n2 
        dp = [[float("-inf")] * (n2+1) for _ in range(n1+1)]

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1): 
                dp[i][j] = max(
                    dp[i+1][j], 
                    dp[i][j+1], 
                    nums1[i] * nums2[j],
                    nums1[i] * nums2[j] + dp[i+1][j+1]
                )
                
        return dp[0][0]


    