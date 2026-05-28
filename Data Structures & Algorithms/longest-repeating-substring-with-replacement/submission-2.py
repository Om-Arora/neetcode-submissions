from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Use a sliding window, and keep a dict of char frequencies.
        When expanding, check if chars other than most common char
        occur at most k times, otherwise shrink the window.
        Shrinking window requires checking what character is now
        the most frequent.
        """
        n = len(s)
        left, right = 0, 0
        count = 0
        seen = defaultdict(int)
        window = 0
        while right < n:
            seen[s[right]] += 1
            count += 1
            letter, num = max(seen.items(), key=lambda x: x[1])
            while k < (count - num):
                # more than k other characters here
                seen[s[left]] -= 1
                count -= 1
                letter, num = max(seen.items(), key=lambda x: x[1])
                left += 1
            right += 1
            window = max(window, right - left)
        return window