class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Given a sorted array where every element appears exactly twice except for one element
        which appears once, return that single element.

        Key property in a sorted array of pairs:
          - Before the single element, pairs start at EVEN indices: (0,1), (2,3), ...
          - After  the single element, pairs start at ODD  indices:  (k, k+1) shifts by one
        We exploit this by always aligning `mid` to an EVEN index and comparing nums[mid] with nums[mid+1].
        """

        # Standard binary search boundaries.
        left = 0
        right = len(nums) - 1

        # Loop until we converge to the single element's index.
        while left < right:
            # Midpoint (avoid potential overflow style; Python doesn't overflow but this is idiomatic).
            mid = (left + right )// 2

            # Force `mid` to be EVEN so that (mid, mid+1) form a candidate pair boundary.
            # If mid is odd, decrement by 1 to make it even.
            if mid % 2 == 1:
                mid -= 1

            # Now compare the pair at positions mid and mid+1.
            if nums[mid] == nums[mid + 1]:
                # If they match, the single element is not in [left..mid+1].
                # All pairs up to mid+1 are "proper" pairs, so we can skip them.
                # Move left past this pair.
                left = mid + 2
            else:
                # If they don't match, the pair is "broken" here,
                # which means the single element is in [left..mid].
                right = mid

        # When left == right, we've narrowed down to the single element.
        return nums[left]

        # Time Complexity is O(log(n))
        # Space Complexity is O(1)

