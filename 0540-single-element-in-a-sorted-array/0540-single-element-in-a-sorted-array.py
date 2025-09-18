class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        # We binary search until the search space collapses to a single element.
        while lo < hi:
            mid = lo + (hi - lo) // 2

            # Ensure mid always points to the *first element of a pair*
            # (i.e., an even index). This makes reasoning easier because
            # we can always compare nums[mid] with nums[mid+1].
            if mid % 2 == 1:
                mid -= 1

            # Case 1: nums[mid] == nums[mid+1]
            # -> Pairing is correct up to this point (no disruption yet).
            # -> That means the single element must lie *after* this pair.
            # -> Since mid and mid+1 form a valid pair, skip them both.
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                # Case 2: nums[mid] != nums[mid+1]
                # -> The "pairing rule" breaks here, so the single element
                #    must be at mid or somewhere to the left.
                hi = mid

            # Invariant maintained:
            #   The single element always lies on the side with an odd length.

        # When lo == hi, we've converged on the single element.
        return nums[lo]