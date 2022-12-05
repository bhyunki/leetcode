class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfsIslands(i:int, j:int):
            if grid[i][j] == '0':
                return

            grid[i][j] = '0'

            if i-1 >= 0:
                dfsIslands(i-1, j)
            if i+1 < len(grid):
                dfsIslands(i+1, j)
            if j-1 >= 0:
                dfsIslands(i, j-1)
            if j+1 < len(grid[0]):
                dfsIslands(i, j+1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfsIslands(i,j)
                    cnt+=1

        return cnt
