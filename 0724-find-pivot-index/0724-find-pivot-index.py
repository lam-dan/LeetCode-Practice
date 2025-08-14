class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        running_total = 0
        for i in range(len(nums)):
            running_total += nums[i - 1] if i > 0 else 0
            if running_total == (total - running_total - nums[i]):
                return i
        return -1

