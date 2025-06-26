from collections import deque

class Solution:
    def hasPath(self, maze, start, destination):
        rows, cols = len(maze), len(maze[0])
        
        queue = deque([start])  # BFS queue holds stop positions to explore
        seen = set()  # Tracks positions we've already processed to prevent cycles
        
        # Possible directions to roll: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            row, col = queue.popleft()  # Get next stop position to explore

            # Base Case: If we reach the destination, return True
            if [row, col] == destination:
                return True

            # Explore all four directions from current stop position
            for dr, dc in directions:
                next_row, next_col = row, col  # Reset to current stop position

                # Roll continuously in the chosen direction until hitting a wall or boundary
                while 0 <= next_row + dr < rows and 0 <= next_col + dc < cols and maze[next_row + dr][next_col + dc] == 0:
                    next_row += dr
                    next_col += dc

                # The ball stops just before the wall or boundary
                # Only queue the stop position if it hasn't been visited yet
                if (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))  # Mark position as visited
                    queue.append((next_row, next_col))  # Add stop position to BFS queue

        # If queue is exhausted and destination wasn't reached, no valid path exists
        return False