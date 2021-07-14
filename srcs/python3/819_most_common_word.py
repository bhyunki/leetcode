class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d=collections.defaultdict(int)
        regex = re.compile(r'\W+')
        for word in regex.split(paragraph):
            l = word.lower()
            if l not in banned:
                d[l]+=1

        return max(d, key=d.get)
