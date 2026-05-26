class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i] = best profit made from day i to end
        # dp[i] = max(dp[i+1], -> nothing today
        #             (sell on some jth day - buy today) + dp[j+1]
        # )
        # O(n^2) solutions
        n = len(prices)
        dp = [None for _ in range(n + 1)]
        def helper(i):
            if i >= n:
                return 0
            if dp[i] is None:
                l = [
                    helper(j+1) + (prices[j] - prices[i])
                    for j in range(i, n)
                ]
                l.append(0)
                dp[i] = max(l)
                dp[i] = max(dp[i], helper(i+1))
            return dp[i]
        
        return helper(0)