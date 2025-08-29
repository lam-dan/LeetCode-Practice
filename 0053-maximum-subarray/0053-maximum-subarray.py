class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            new_max = current_max + nums[i]
            if new_max > nums[i]:
                current_max = new_max
            else:
                current_max = nums[i]
            if current_max > max_num:
                max_num = current_max

        return max_num