class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Check for empty matrix or empty row; return empty list if true
        if not mat or not mat[0]:
            return []

        # Get the number of rows in the matrix
        rows = len(mat)
        # Get the number of columns in the matrix
        cols = len(mat[0])

        # Initialize the current row index
        r = 0
        # Initialize the current column index
        c = 0
        # Initialize direction: 1 means moving up-right, 0 means moving down-left
        direction = 1
        # Initialize result list to store elements in diagonal order
        result = []

        # Loop until we've visited all elements in the matrix
        while len(result) < rows * cols:
            # Append the current matrix element to result; we start at top-left cell (0, 0)
            result.append(mat[r][c])

            # If moving in the up-right direction
            if direction == 1:
                # Moving up-right (↗)
                if c == cols - 1:
                    # We've hit the right boundary (e.g., cells 3, 6, 9)
                    # Can't move further right — move down to the next row
                    r += 1
                    direction = 0  # Change direction to down-left (↙)
                elif r == 0:
                    # We've hit the top boundary (e.g., cells 1, 2, 3)
                    # Can't move further up — move right to the next column
                    c += 1
                    direction = 0  # Change direction to down-left (↙)
                else:
                    # Normal up-right move: go one row up, one column right
                    r -= 1
                    c += 1
            else:
                # Moving down-left (↙)
                if r == rows - 1:
                    # We've hit the bottom boundary (e.g., cells 7, 8, 9)
                    # Can't move further down — move right to the next column
                    c += 1
                    direction = 1  # Change direction to up-right (↗)
                elif c == 0:
                    # We've hit the left boundary (e.g., cells 1, 4, 7)
                    # Can't move further left — move down to the next row
                    r += 1
                    direction = 1  # Change direction to up-right (↗)
                else:
                    # Normal down-left move: go one row down, one column left
                    r += 1
                    c -= 1
        # Return the final result list with diagonal order traversal
        return result


        # Time Complexity: O(m * n)
        # - We visit each of the m * n elements exactly once.
        # Space Complexity: O(1) additional space (excluding the output list)
        # - We use only a fixed number of variables. The output list takes O(m * n) space.

                

