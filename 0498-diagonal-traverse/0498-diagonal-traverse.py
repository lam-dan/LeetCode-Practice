class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Handle the empty matrix case
        if not mat or not mat[0]:
            return []

        rows = len(mat)
        cols = len(mat[0])

        r = 0
        c = 0
        direction = 1 # 1 means moving up-right, 0 means moving down-left
        result = []

        # Continue until we have viisted all elements
        while r < rows and c < cols:
            result.append(mat[r][c]) # Starting at top left cell

            if direction == 1: # Moving up-right
                if c == cols - 1: # Hit up the right boundary
                    # Move down to the next row, change direction
                    r += 1
                    direction = 0
                elif r == 0: # Hit the top boundary
                    # Move right to the next column, change direction
                    c += 1
                    direction = 0
                else:
                    # Move up and to the right
                    r -= 1
                    c += 1
            else: # direction == 0, moving down-left
                if r == rows - 1: # Hit the bottom boundary
                # Move down to the next column, change direction
                    c += 1
                    direction = 1
                elif c == 0: # Hit the left boundary
                    # Move down to the next row, change direction
                    r += 1
                    direction = 1
                else:
                    # Move down and to the left
                    r += 1
                    c -= 1
        return result

                

