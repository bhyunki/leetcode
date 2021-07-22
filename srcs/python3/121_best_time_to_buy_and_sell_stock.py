class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0;
        m = sys.maxsize
        for price in prices:
            m = min(m, price)
            p = max(p, price-m)
        return p
