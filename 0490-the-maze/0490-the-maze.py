from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        
        queue = deque([start])
        seen = set()
        # col = up and down
        # row - up and down
        direction = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            curr_row, curr_col = queue.popleft()

            # Base Case: Correct Destination Return
            if curr_row == destination[0] and curr_col == destination[1]:
                return True

            # Iterate through all four directions
            for r, c in direction:
                next_row, next_col = curr_row, curr_col

                # While we are within boundaries of the
                while next_row >= 0 and next_row < rows and next_col >= 0 and next_col < cols and maze[next_row][next_col] == 0:
                    next_row += r
                    next_col += c
                
                next_row -= r
                next_col -= c

                if (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col))
        
        return False