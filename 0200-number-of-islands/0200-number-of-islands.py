class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        direction = [
            (1,0),
            (-1,0),
            (0,-1),
            (0,1)
        ]

        def dfs(r,c):
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"

            for dr, dc in direction:
                dfs(r + dr, c + dc)
            
            return
            
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count
