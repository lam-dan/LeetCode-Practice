class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            prefix_sum = max(nums[i], prefix_sum + nums[i])
            max_sum = max(prefix_sum, max_sum)
        return max_sum