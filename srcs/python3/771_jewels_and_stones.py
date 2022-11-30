class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum = 0
        d = collections.defaultdict(int)
        for c in stones:
            d[c] += 1
        for c in jewels:
            sum += d[c]
        return sum
