class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append( (v,w) )

        q = [(0, k)]
        dist = defaultdict(list)

        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    heapq.heappush(q, (time+w, v))

        if len(dist) == n:
            return max(dist.values())

        return -1
