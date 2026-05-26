from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for x in s:
            d[x] += 1
        for x in t:
            d[x] -= 1
        
        for k, v in d.items():
            if v != 0:
                return False

        return True