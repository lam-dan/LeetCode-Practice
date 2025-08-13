class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Create an output list of the same length as nums, initialized with zeros.
        # We'll fill this list from the end (largest squares) to the start (smallest squares).
        result = [0] * len(nums)

        # Initialize two pointers:
        # - left starts at the beginning (smallest index)
        # - right starts at the end (largest index)
        left = 0
        right = len(nums) - 1

        # Iterate backwards over result's indices (from last to first).
        # i is the position in result we are currently filling.
        for i in range(len(nums) - 1, -1, -1):
            # Compare the absolute values at both ends.
            # The one with the larger absolute value will produce the larger square.
            if abs(nums[left]) < abs(nums[right]):
                # Right value has the larger absolute value, so use it.
                square = nums[right]
                right -= 1  # Move right pointer inward (one step to the left).
            else:
                # Left value has the larger absolute value, so use it.
                square = nums[left]
                left += 1   # Move left pointer inward (one step to the right).

            # Place the square of the chosen number into the current position in result.
            result[i] = square * square

        # At this point, result is fully filled with sorted squares in ascending order.
        return result
