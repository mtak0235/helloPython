class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if grid[r][c] != 1:
                return
            nonlocal count
            count += 1
            grid[r][c] = 2
            if 0 <= r - 1:
                dfs(r - 1, c)
            if r + 1 < m:
                dfs(r + 1, c)
            if 0 <= c - 1:
                dfs(r, c - 1)
            if c + 1 < n:
                dfs(r, c + 1)
        
        max_count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = 0
                    dfs(i, j)
                    max_count = max(count, max_count)
        return max_count
