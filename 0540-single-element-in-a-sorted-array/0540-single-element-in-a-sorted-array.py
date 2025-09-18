class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if nums[mid] == nums[mid + 1]:
                if (right - mid) % 2 == 0: # Check if you have even length
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                if (right - mid) % 2 == 0: # Check if you have even length
                    right = mid - 2
                else:
                    left = mid + 1

        return nums[left]
