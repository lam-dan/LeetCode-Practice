class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if mid % 2 == 0:
                # mid is even → should be the first of a pair; compare right neighbor
                if nums[mid] == nums[mid + 1]:
                    # pair intact → single is to the right of this pair
                    left = mid + 2
                else:
                    # pair broken (or mid is the single) → keep left half including mid
                    right = mid
            else:
                # mid is odd → should be the second of a pair; compare left neighbor
                if nums[mid] == nums[mid - 1]:
                    # pair intact → single is to the right
                    left = mid + 1
                else:
                    # pair broken → single is to the left
                    right = mid - 1

        return nums[left]