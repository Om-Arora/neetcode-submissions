from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for x in strs:
            c = [0] * 26
            for i in x:
                c[ord('a') - ord(i)] += 1
            d[tuple(c)].append(x)

        return [x for x in d.values()]
        