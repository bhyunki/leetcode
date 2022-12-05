class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        r = []
        c = collections.Counter(nums)
        
        for n in c:
            heapq.heappush(h, (-c[n], n))
        
        for i in range(k):
            t = heapq.heappop(h)
            r.append(t[1])
            
        return r
