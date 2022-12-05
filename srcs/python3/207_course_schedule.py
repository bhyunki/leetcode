class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        traced=set()
        visited=set()
        d = defaultdict(list)
        for x,y in prerequisites:
            d[x].append(y)

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for c in d[i]:
                if not dfs(c):
                    return False
            traced.remove(i)
            
            visited.add(i)
            return True

        for k in list(d):
            if not dfs(k):
                return False

        return True
