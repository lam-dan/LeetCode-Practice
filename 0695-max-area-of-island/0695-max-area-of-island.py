class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        self.count = 0

        def dfs(r,c):
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                grid[r][c] == 0
            ):
                return
            grid[r][c] = 0
            self.count += 1
            dfs(r + 1, c) 
            dfs(r - 1,c)  
            dfs(r,c + 1) 
            dfs(r,c - 1)

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                self.count = 0
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, self.count)
        return max_area
        
        






        

