class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)
        for w in strs:
            l = list(w)
            l.sort()
            d[''.join(l)].append(w)
        answer=[]
        for i in d:
            answer.append(sorted(d[i]))
        return sorted(answer, key=len)
