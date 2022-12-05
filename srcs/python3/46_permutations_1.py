class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def dfs(p:List, n:List):
            if len(n) ==0:
                results.append(p[:])
                return
            
            for c in n:
                next = n[:]
                next.remove(c)
                p.append(c)
                dfs(p, next)
                p.pop()

        dfs([], nums)
        return results
