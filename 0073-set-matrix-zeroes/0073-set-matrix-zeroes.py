class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_col_has_zero = False

        # Iterate through a the "INNER" 2D matrix excluding the first column and row
        # when a cell is detected as a 0, mark the corresponding row and col 0s
        for r in range(rows):
            # If any value in the first column is 0, set the flag to true to do some processing later
            if matrix[r][0] == 0:
                first_col_has_zero = True
            for c in range(1, cols): # Iterate through inner cells
                if matrix[r][c] == 0: # If a zero is detected in the cell
                    matrix[r][0] = 0 # Mark the outer row as 0, the row in the first column
                    matrix[0][c] = 0 # Mark the outer col as 0, the col in the first row

        # Iterate through the "INNER" 2D matrix again and zero out all cells in the rows and cols 
        # that were marked earlier
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # Handle the first row now since you don't want to handle them earlier as they
        # might be overrided through the loop right before
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0
        
        # Handle the first col last to make sure they are zeroed out as well
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0

        return matrix






        
        
