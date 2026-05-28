from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, 0
        pq = []
        count = 0
        seen = defaultdict(int)
        window = 0
        while right < n:
            seen[s[right]] += 1
            count += 1
            letter, num = max(seen.items(), key=lambda x: x[1])
            print(left, right)
            while k < (count - num):
                print(left, count, num)
                # more than k other characters here
                seen[s[left]] -= 1
                count -= 1
                letter, num = max(seen.items(), key=lambda x: x[1])
                left += 1
            right += 1
            window = max(window, right - left)
        return window