class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        index = self.binary_search_index(matrix, target)
        array_with_num = self.binary_search_target(matrix[index], target)
        return  array_with_num

    def binary_search_index(self, array:List, target:int):
        left = 0
        right = len(array) - 1

        # Problem statement implies left most insertion point, but in this case,
        # left <= right	ensures the search space is fully exhausted and the last candidate index is processed
        # left < right	May exit early, skipping valid candidate rows
        while left <= right:
            mid = (left + right) // 2
            if array[mid][0] == target:
                return mid
            elif array[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1 # Handles edge case where left is basically
        # matrix = [
        #     [1, 2, 3],    # Row 0
        #     [5, 6, 7],    # Row 1
        #     [9, 10, 11]   # Row 2
        # ]

        # 1. Target Lies Between Two Rows (Standard Floor Search Case)
        # Target = 7
        # returns left = 2 incorrectly

        # 2. Target Smaller than All Rows (Overshoot Below)
        # Target = 12
        # returns left = 2 incorrectly

        # 3. Target Larger than All Rows (Overshoot Above)
        # Target = 12
        # returns left = 2 incorrectly

    def binary_search_target(self, array:List, target:int):
        left = 0
        right = len(array) - 1

        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            elif array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


