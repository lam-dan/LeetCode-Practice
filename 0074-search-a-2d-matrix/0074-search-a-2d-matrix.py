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

        while left <= right:
            mid = (left + right) // 2
            if array[mid][0] == target:
                return mid
            elif array[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1

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


