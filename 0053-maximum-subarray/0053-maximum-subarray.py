class Solution:
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = float('-inf')

        for num in nums:
            curr_sum += num               # Add current number
            max_sum = max(max_sum, curr_sum)  # Track best seen so far

            # If the running sum becomes negative, reset to 0
            # because a negative sum would only hurt any future subarray.
            if curr_sum < 0:
                curr_sum = 0

        return max_sum