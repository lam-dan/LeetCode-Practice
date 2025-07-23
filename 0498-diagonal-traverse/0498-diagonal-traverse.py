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
                # If we've hit the right boundary (last column)
                if c == cols - 1:
                    # Move down to the next row
                    r += 1
                    # Change direction to down-left
                    direction = 0
                # If we've hit the top boundary (first row)
                elif r == 0:
                    # Move right to the next column
                    c += 1
                    # Change direction to down-left
                    direction = 0
                else:
                    # Otherwise, move up one row and right one column
                    r -= 1
                    c += 1
            else:
                # If moving in the down-left direction

                # If we've hit the bottom boundary (last row)
                if r == rows - 1:
                    # Move right to the next column
                    c += 1
                    # Change direction to up-right
                    direction = 1
                # If we've hit the left boundary (first column)
                elif c == 0:
                    # Move down to the next row
                    r += 1
                    # Change direction to up-right
                    direction = 1
                else:
                    # Otherwise, move down one row and left one column
                    r += 1
                    c -= 1

        # After collecting all elements, return the result list
        return result

        # Time Complexity: O(m * n)
        # - We visit each of the m * n elements exactly once.
        # Space Complexity: O(1) additional space (excluding the output list)
        # - We use only a fixed number of variables. The output list takes O(m * n) space.

                

