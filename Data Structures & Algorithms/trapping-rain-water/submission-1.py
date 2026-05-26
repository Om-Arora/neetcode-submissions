class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # scan least heights
        left = []
        best = 0
        for i in range(n):
            best = max(best, height[i])
            left.append(best)
        # print(left)
        
        # scan most heights
        # rev = list(reversed(height))
        right = [0 for _ in range(n)]
        best = 0
        for i in range(n):
            best = max(best, height[n-i-1])
            right[n-i-1] = best
        # print(right)

        water = 0
        for i in range(n):
            if height[i] < min(left[i], right[i]):
                water += min(left[i], right[i]) - height[i]
        return water
        