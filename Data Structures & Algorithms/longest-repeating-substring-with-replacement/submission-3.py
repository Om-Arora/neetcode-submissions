from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Use a sliding window, and keep a dict of char frequencies.
        When expanding, check if chars other than most common char
        occur at most k times, otherwise shrink the window.
        Shrinking window requires checking what character is now
        the most frequent.
        ---
        Optimization: 
        1. The window never needs to shrink, so don't need a while loop
        inside to shrink the window. Slide the window by to the right,
        and if the new window isn't valid, move on - we already have a
        valid window of this size. It doesn't make sense to shrink it.
        2. A valid window always has 
            window_size - max_count <= k
        where k is fixed.
        For the window size to grow, max_count must grow accordingly.
        Instead of finding the maximum frequency character in every run,
        we can simply find the max of max_count and the newly seen char.
        If the newly seen char exceeds the max_count, we have a new highest
        frequency character, and hence can increase the window size.
        Otherwise, max_count remains where it is, and we do not end up
        increasing the window size.
        """
        left, right = 0, 0
        seen = defaultdict(int)
        max_count = 0
        while right < len(s):
            seen[s[right]] += 1
            max_count = max(max_count, seen[s[right]])
            if ((right - left + 1) - max_count) > k:
                # more than k other characters here
                seen[s[left]] -= 1
                left += 1
            right += 1
        return right - left