from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        most_common = c.most_common(1)
        if len(most_common) == 1 and most_common[0][1] > 1:
            return True
        return False
        