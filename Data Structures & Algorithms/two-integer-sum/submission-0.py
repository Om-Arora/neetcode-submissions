from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(lambda: -1)
        for i, n in zip(range(len(nums)), nums):
            if d[target - n] != -1:
                return [d[target - n], i]
            else:
                d[n] = i
        return []