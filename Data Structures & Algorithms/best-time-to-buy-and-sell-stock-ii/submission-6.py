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
        # O(n) solution, bottom up approach, space optimized
        n = len(prices)
        prev = [0, prices[n-1]]

        for day in range(n - 2, -1, -1):
            prev[0], prev[1] = max(prev[0], prev[1] - prices[day]), max(prev[1], prev[0] + prices[day])

        return prev[0]