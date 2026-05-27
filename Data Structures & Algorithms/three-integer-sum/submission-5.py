class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 1):
            if i > 0 and nums[i - 1] == nums[i]: continue
            left, right = i + 1, n - 1
            need = - nums[i]
            while left < right:
                s = nums[left] + nums[right]
                if s > need:
                    # need s to be smaller
                    right -= 1
                elif s < need:
                    # need s to be bigger
                    left += 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

        return result