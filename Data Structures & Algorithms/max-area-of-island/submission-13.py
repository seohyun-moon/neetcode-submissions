class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        row, col = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == row or c == col or
                (r, c) in visit or grid[r][c] == 0):
                return 0
            visit.add((r, c))

            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))            

        area = 0
        for i in range(row):
            for j in range(col):
                area = max(area, dfs(i, j))
                    
        return area