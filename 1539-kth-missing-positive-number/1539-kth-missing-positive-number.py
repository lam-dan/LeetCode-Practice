class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        # Binary search for the first index where missing numbers before arr[i] >= k
        while left <= right:
            mid = (left + right) // 2

            missing = arr[mid] - (mid + 1)  # Number of missing nums before arr[mid]
            # We use arr[i] - (i + 1) to calculate how many values are missing up to index i, 
            # based on how far arr[i] has jumped ahead from its ideal position. This only works 
            # because the array is strictly increasing — every element is larger than the previous, 
            # so missing counts grow. That lets us binary search over the index and compute the k-th 
            # missing number as k + left.

            if missing < k:
                left = mid + 1  # Not enough missing numbers yet
            else:
                right = mid - 1  # Too many missing numbers, go left

        # After binary search:
        # - 'left' is the smallest index where missing numbers ≥ k
        # - 'k + left' gives the actual k-th missing number
        return k + left

        # If we had an imaginary array that only contained the missing numbers, 
        # then k would directly give us the value of the k-th missing number.
        # However, the real number line also includes valid (non-missing) numbers from the 
        # input array arr, which we must "step over" as we count missing values. During binary search, 
        # left ends up being the count of how many real (non-missing) values we’ve seen before reaching 
        # the k-th missing number. These values are not part of the missing sequence but still count 
        # when moving along the full number line. Therefore, we need to add those left valid numbers 
        # to our target k to get the actual number in the number line: k + left.


