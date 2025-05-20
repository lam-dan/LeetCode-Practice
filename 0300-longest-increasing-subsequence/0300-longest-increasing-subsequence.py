class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums = [10,9,2,5,3,7]
        dp = [1] * len(nums)
        # dp = [1,1,1,1,1,1]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) # dp = [1,1,1,2,2,3]
        return max(dp) # max(dp) = 3

        # Time Complexity = O(n^2)