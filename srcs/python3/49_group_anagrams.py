class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)
        for w in strs:
            l = list(w)
            l.sort()
            d[''.join(l)].append(w)
        return d.values()
