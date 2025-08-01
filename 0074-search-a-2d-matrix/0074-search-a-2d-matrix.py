class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        r = len(matrix)
        c = len(matrix[0])

        left = 0
        right = r * c - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert mid index back to 2D matrix coordinates:
            row = mid // c # Row index (integer division)
            col = mid % c # Column index (modulo gives offset within row)

            mid_val = matrix[row][col]  # Actual value at that 2D position

            # Debug: Print mid and corresponding matrix value
            # print(f"Checking mid index {mid} -> matrix[{row}][{col}] = {mid_val}")

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False

