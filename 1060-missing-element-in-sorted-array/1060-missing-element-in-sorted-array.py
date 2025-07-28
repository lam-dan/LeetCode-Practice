class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1

        # Binary search to find the smallest index such that
        # the number of missing elements before that index is at least k
        while left <= right:
            mid = (left + right) // 2

            # Calculate how many numbers are missing up to index `mid`
            # If the array had no missing numbers, then nums[mid] should equal nums[0] + mid
            # So the number of missing values is the difference between the actual value
            # and the expected value: nums[mid] - nums[0] - mid
            #
            # This works because:
            # - nums[mid] - nums[0] gives the number of steps we've moved numerically
            # - subtracting mid (which is 0-based) tells us how many numbers should exist between nums[0] and nums[mid]
            # The result is the number of missing numbers between nums[0] and nums[mid]
            missing = nums[mid] - nums[0] - mid

            if missing < k:
                # Not enough missing numbers yet → need to go right
                left = mid + 1
            else:
                # We've passed or reached the k-th missing number → try earlier index
                right = mid - 1

        # At this point, left tells us how many valid (non-missing) numbers we've passed
        # before we reach the location where the k-th missing number belongs.

        # So the total number of steps from nums[0] = k (missing) + left (valid)
        # We subtract 1 to avoid overcounting since both counts include the stopping point
        return nums[0] + k + left - 1

