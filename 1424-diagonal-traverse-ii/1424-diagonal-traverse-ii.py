class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Get total number of rows in the jagged 2D list
        rows = len(nums)

        # This will store the final diagonal traversal order
        result = []

        # Initialize queue for BFS starting from top-left cell (0, 0)
        queue = deque([(0, 0)])

        # Perform BFS traversal
        while queue:
            r, c = queue.popleft()  # Get the next cell coordinates from the queue
            result.append(nums[r][c])  # Visit and collect the current cell's value

            # === KEY LOGIC ===
            # At each cell, we may enqueue:
            # 1. The cell directly below: (r+1, c)
            # 2. The cell directly to the right: (r, c+1)

            # STEP 1: Add the cell below (r+1, c) ONLY if:
            # - We're at the first column of a diagonal (c == 0)
            # - And the row below exists (r + 1 < rows)
            if c == 0 and r + 1 < rows:
                queue.append((r + 1, c))

            # STEP 2: Add the cell to the right (r, c+1) ONLY if:
            # - There is a next column in the current row
            # - Since nums is jagged, use len(nums[r]) instead of fixed column size
            if c + 1 < len(nums[r]):
                queue.append((r, c + 1))

        # After visiting all reachable cells, return the result list
        return result

        # Time Complexity: O(n)
        # - We visit each of the n elements exactly once during BFS traversal.

        # Space Complexity: O(√n)
        # - The queue holds at most one diagonal at a time.
        # - The longest diagonal possible has size O(√n), because:
        #     - A diagonal of size k requires at least O(k^2) elements to support it.
        #     - So a grid of size n can only support diagonals up to length O(√n).
        # - The result list uses O(n) space, but this is not counted as auxiliary space.

        





