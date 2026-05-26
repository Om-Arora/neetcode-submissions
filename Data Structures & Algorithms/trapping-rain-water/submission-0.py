class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = []
        best = 0
        for i in range(n):
            best = max(best, height[i])
            left.append(best)
        # print(left)
        
        rev = list(reversed(height))
        right = []
        best = 0
        for i in range(n):
            best = max(best, rev[i])
            right.append(best)
        right.reverse()
        # print(right)

        water = 0
        for i in range(n):
            if height[i] < min(left[i], right[i]):
                water += min(left[i], right[i]) - height[i]
        return water
        