class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    water += maxLeft - height[left]
            else:
                right -= 1
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    water += maxRight - height[right]

        return water