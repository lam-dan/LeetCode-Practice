class Solution:
    def maxSubArray(self, nums):
        prefix_sum = 0
        min_prefix = 0
        max_subarray = float('-inf')

        for num in nums:
            prefix_sum += num
            min_prefix = min(min_prefix, prefix_sum)
            max_subarray = max(max_subarray, prefix_sum - min_prefix)
        return max_subarray