class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        left = matrix[0][0] # Top left of the matrix
        right = matrix[rows - 1][cols - 1] # Bottom right of the matrix

        #Binary Search
        # We use 'left < right' instead of 'left <= right'
        # because we are searching on value space (not index space).
        # The loop terminates when left == right, at which point we've narrowed
        # the value down to the kth smallest.
        while left < right:
            mid = (left + right) // 2
            # Count how many numbers in the matrix are less than or equal to mid
            count = self.countLessEqual(matrix, mid)

            # If count is enough (>= k), mid could be the kth smallest
            # but we keep searching the left side to find the smallest such number
            if count >= k:
                right = mid
            else:
                # If count is too small, search in the higher half
                left = mid + 1

        # left == right is the kth smallest element after convergence
        return left

    def countLessEqual(self, matrix, target):
        """
        Binary search in value space to find the kth smallest number in a sorted matrix.
        Uses a lower-bound template to find the smallest number such that count >= k.
        """
        count = 0
        rows = len(matrix)
        cols = len(matrix[0])

        # Starting at the bottom left
        i = rows - 1 # row index
        j = 0 # column index

        # Continue traversal while i and j are within the matrix boundaries
        while i >= 0 and j < cols:

            if matrix[i][j] <= target:
                # All elements in current column up to row i are <= target
                count += i + 1
                j += 1 # Column - Index - Move right to next column
            else:
                i -= 1 # Rows - Move up to the previous row
        return count






