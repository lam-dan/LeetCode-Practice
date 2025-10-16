class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_element = float('inf')

        while left <= right:
            mid = (left + right) // 2
            # Case 1: The entire segment is sorted
            # If left <= mid <= right, then nums[left] <= nums[mid] <= nums[right]
            # means no rotation inside this range
            if nums[left] <= nums[mid] <= nums[right]:
                # So the smallest element is definitely nums[left]
                min_element = min(min_element, nums[left])
                return min_element
            # Case 2: Left half is sorted
            elif nums[left] <= nums[mid]:
                # Since left half is sorted, nums[left] is the smallest in that half
                min_element = min(min_element, nums[left])
                # Search in the unsorted right half
                left = mid + 1
            # Case 3: Right half is sorted
            else:
                # Since rotation lies in the left half, check nums[mid]
                min_element = min(min_element, nums[mid])
                right = mid - 1
        return min_element