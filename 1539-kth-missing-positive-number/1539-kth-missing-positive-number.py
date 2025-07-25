class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Can't apply binary search since target is missing
        # Can't apply binary search on answers - only applicable on min or max
        # Not the case
        # Need to figure out where the answer fits between the the numbers in the arr
        # Figure out the 2 nearby indexes
        # Figure out the missing numbers at each index by taking current value and subtracting
        # from previous value
        #  0 1 2 3 4
        # [2,3,4,7,11]
        # [1,1,1,3,6]
        # Step 1: Calculate the number of missing positive integers
        # before each element in arr.
        # For example, if arr[i] = 7 and i = 3 (4th element),
        # then 6 positive numbers should be there by index 3 (1-based),
        # so 7 - (i + 1) = 7 - 4 = 3 numbers are missing.
        missing_numbers = [0] * len(arr)
        for i in range(len(arr)):
            missing_numbers[i] = arr[i] - i - 1

        # Binary search to find the smallest index such that
        # missing_numbers[index] >= k
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if missing_numbers[mid] < k:
                # Not enough missing numbers before this index — look to the right
                left = mid + 1
            else:
                # Too many missing numbers — look to the left
                right = mid - 1

        # After the loop ends:
        # - 'left' is the first index in arr such that missing_numbers[left] >= k
        # - 'right' is the index just before it (i.e., last one where missing_numbers < k)

        # Case 1: If left == 0, then the k-th missing number occurs before the first element
        if left == 0:
            return k  # Just return the k-th number directly (since nothing is missing yet)

        # Case 2: General case
        # missing up to arr[right] is missing_numbers[right]
        # We need (k - missing_numbers[right]) more steps beyond arr[right]
        return arr[right] + (k - missing_numbers[right])



