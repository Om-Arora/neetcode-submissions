from bisect import bisect_left as binsearch

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set()
        for i in range(n):
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
                    triplet = (nums[i], nums[left], nums[right])
                    if triplet not in seen:
                        seen.add(triplet)
                    left += 1


        return [list(x) for x in seen]