class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # mid pairs with right neighbor → mid is 1st of its pair
            if nums[mid] == nums[mid + 1]:
                right_half_len = right - mid + 1  # inclusive [mid..right]
                if right_half_len % 2 == 0:
                    # even → single on LEFT
                    right = mid - 1
                else:
                    # odd → single on RIGHT
                    left = mid + 2

            # mid pairs with left neighbor → mid is 2nd of its pair
            elif nums[mid] == nums[mid - 1]:
                right_half_len = right - mid + 1  # inclusive [mid..right]
                if right_half_len % 2 == 0:
                    # even → single on RIGHT  (Fix 2: this was flipped)
                    left = mid + 1
                else:
                    # odd → single on LEFT
                    right = mid - 2
            else:
                right = mid

        return nums[left]


