class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = self.binary_search_index(matrix, target)
        result = self.binary_search_target(matrix[index], target)
        return result

    def binary_search_index(self, array, target):
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
        return right

    def binary_search_target(self, array, target):
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


