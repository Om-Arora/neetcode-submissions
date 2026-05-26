class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i] = best profit made from day i to end
        # dp[i] = max(dp[i+1], -> nothing today
        #             (sell on some jth day - buy today) + dp[j+1]
        # )
        # O(n^2) solutions
        n = len(prices)
        dp = [0 for _ in range(n + 1)]
        
        for i in range(n-1, -1, -1):
            l = [dp[j+1] + (prices[j] - prices[i]) for j in range(i+1, n)]
            dp[i] = max(dp[i], dp[i+1], *l)
        
        return dp[0]