class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 2 pointers

        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        i = len(nums) - 1

        while i >= 0:
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
            i -= 1
        return result
        # Time Complexity is O(n)
        # Space Complexity is O(n)

