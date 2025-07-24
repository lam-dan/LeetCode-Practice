class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Standard binary search loop
        while left <= right:
            mid = (left + right) // 2

            # Base case: found the target
            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            # If left pointer is less than right pointer
            # then Left half is sorted
            if nums[left] <= nums[mid]: 
                # Check if target is within the left sorted range
                if nums[left] <= target < nums[mid]:
                    # Target is in the left half — discard right half
                    right = mid - 1
                else:
                    # Target is not in the left half — search right half
                    left = mid + 1
            else: # Right half is sorted
                # Check if target is within the right sorted range
                if nums[mid] < target <= nums[right]:
                    # Target is in the right half — discard left half
                    left = mid + 1
                else:
                    # Target is not in the right half — search left half
                    right = mid - 1
        # Target not found in the array
        return -1



