class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window solution
        n = len(s)
        if n == 0:
            return 0
        left, right = 0, 0
        seen = set()
        length = 0
        while right < n:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            length = max(right - left, length)
        return length