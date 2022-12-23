class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        
        n = len(prices)
        dp = {}

        def dfs(i, buying) -> int:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying: 
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else: 
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        return dfs(0,True)
