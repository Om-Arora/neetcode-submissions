class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] = best profit made from day i to end 
        #            when not holding stock
        # dp[i][1] = best profit made from day i to end
        #            when holding stock
        # dp[i][0] = max(dp[i+1][0], -> nothing today
        #                dp[i+1][1] - price[i] -> buy today
        # )
        # dp[i][1] = max(dp[i+1][1], -> nothing today
        #                dp[i+1][0] + price[i]
        # )
        # O(n) solution, bottom up approach
        n = len(prices)
        dp = [[None, None] for _ in range(n)]
        dp[n - 1][0] = 0
        dp[n - 1][1] = prices[n - 1]

        for day in range(n - 2, -1, -1):
            dp[day][0] = max(dp[day+1][0], dp[day+1][1] - prices[day])
            dp[day][1] = max(dp[day+1][1], dp[day+1][0] + prices[day])

        return dp[0][0]