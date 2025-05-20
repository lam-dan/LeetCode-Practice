class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # Every element is at least an LIS of 1

        # Iterate through each number
        for i in range(n):
            # Iterate through all the values up to n
            for j in range(i):
                # check current value against previous values up to i
                # if current number is greater than previous values up to i
                if nums[i] > nums[j]:
                    # Update the current DP table by taking the max
                    # Because we're trying to build the LIS ending at i, by looking at the best LIS before i that can be extended.
# So we are not growing dp[i] itself, but seeing what we can inherit from earlier LIS chains (dp[j]) and then add 1 if we can extend it with nums[i].
                    # "What is the longest increasing subsequence that I can end at nums[i]?"
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        