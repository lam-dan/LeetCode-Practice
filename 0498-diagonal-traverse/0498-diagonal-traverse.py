class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Handle the empty matrix case
        if not mat or not mat[0]:
            return []

        N = len(mat)
        M = len(mat[0])

        row = 0
        column = 0
        direction = 1 # 1 means moving up-right, 0 means moving down-left
        result = []

        # Continue until we have viisted all elements
        while row < N and column < M:
            result.append(mat[row][column])

            if direction == 1: # Moving up-right
                if column == M - 1: # Hit up the right boundary
                    # Move down to the next row, change direction
                    row += 1
                    direction = 0
                elif row == 0: # Hit the top boundary
                    # Move right to the next column, change direction
                    column += 1
                    direction = 0
                else:
                    # Move up and to the right
                    row -= 1
                    column += 1
            else: # direction == 0, moving down-left
                if row == N - 1: # Hit the bottom boundary
                # Move down to the next column, change direction
                    column += 1
                    direction = 1
                elif column == 0: # Hit the left boundary
                    # Move down to the next row, change direction
                    row += 1
                    direction = 1
                else:
                    # Move down and to the left
                    row += 1
                    column -= 1
        return result

                

