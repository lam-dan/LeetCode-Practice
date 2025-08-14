class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            if nums[i] > lower:
                result.append([lower, nums[i] - 1])

            lower = nums[i] + 1
        if lower <= upper:
            result.append([lower, upper])
        return result

        # Time Complexity is O(n)
        # Space Complexity is O(1) no new space created