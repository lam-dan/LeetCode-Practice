class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if mid % 2 == 0:
                # mid is even → should be the first element of a pair
                if nums[mid] == nums[mid + 1]:
                    # Pair is intact → single is on the right
                    lo = mid + 2
                else:
                    # Pair breaks here → single is at mid or to the left
                    hi = mid
            else:
                # mid is odd → should be the second element of a pair
                if nums[mid] == nums[mid - 1]:
                    # Pair is intact → single is on the right
                    lo = mid + 1
                else:
                    # Pair breaks here → single is to the left
                    hi = mid - 1

        return nums[lo]