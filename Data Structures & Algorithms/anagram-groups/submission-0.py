from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for x in strs:
            # m log m where m is length of longest string
            y = "".join(sorted(x))
            d[y].append(x)
        print(d)

        return [x for x in d.values()]
