class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for l in range(len(nums) - k + 1):
            m = max(nums[l:l+k])
            result.append(m)

        return result