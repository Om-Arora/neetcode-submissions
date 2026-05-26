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
        # O(n) solution
        n = len(prices)
        dp = [[None, None] for _ in range(n)]
        dp[-1][0] = 0
        dp[-1][1] = prices[-1]
        
        def profit(day, bought):
            if dp[day][bought] is None:
                if bought == 0:
                    dp[day][0] = max(profit(day+1, 0), profit(day+1, 1) - prices[day])
                else:
                    dp[day][1] = max(profit(day+1, 1), profit(day+1, 0) + prices[day])
            return dp[day][bought]
        
        return profit(0, 0)