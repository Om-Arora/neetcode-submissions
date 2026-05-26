class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # scan least heights
        left = []
        right = [0 for _ in range(n)]
        bestL = 0
        bestR = 0
        for i in range(n):
            bestL = max(bestL, height[i])
            bestR = max(bestR, height[n-i-1])
            left.append(bestL)
            right[n-i-1] = bestR

        water = 0
        for i in range(n):
            if height[i] < min(left[i], right[i]):
                water += min(left[i], right[i]) - height[i]
        return water
        