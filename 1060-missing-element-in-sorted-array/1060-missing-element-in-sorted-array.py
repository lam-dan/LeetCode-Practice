class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1

        # Binary search to find the smallest index such that
        # the number of missing elements before that index is at least k
        while left <= right:
            mid = (left + right) // 2

            # Calculate how many numbers are missing between nums[0] and nums[mid]
            # Formula: nums[mid] - nums[0] - mid
            # Because in a perfect sequence with no missing values:
            # nums[mid] should equal nums[0] + mid
            missing = nums[mid] - nums[0] - mid

            if missing < k:
                # Not enough missing values yet → go right
                left = mid + 1
            else:
                # Too many or just enough → go left
                right = mid - 1

        # At this point, left tells us how many valid (non-missing) numbers we've passed
        # before we reach the location where the k-th missing number belongs.

        # So the total number of steps from nums[0] = k (missing) + left (valid)
        # We subtract 1 to avoid overcounting since both counts include the stopping point
        return nums[0] + k + left - 1

