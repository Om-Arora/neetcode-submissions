class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1
        s = numbers[first] + numbers[last]
        while first < last and s != target:
            s = numbers[first] + numbers[last]
            if s < target:
                first += 1
            elif s > target:
                last -= 1
        return [first+1, last+1]

