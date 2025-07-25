class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        # This approach works because we're using binary search to locate the position (left) in the original 
        # sorted array of non-missing numbers where the k-th missing number would conceptually "fit."
        # Think of the full number line from 1 upward. Some numbers are present in arr, and some are missing. 
        # We're essentially trying to find the point in arr where the count of missing numbers catches up to k.
        # Binary search helps us find that "gap" between two existing (non-missing) numbers in arr where the k-th 
        # missing number belongs.
        # The index left tells us how many valid (non-missing) values we've passed in arr before reaching 
        # the point where the k-th missing number would fall in the number line.
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

        return k + left

        # If we had an imaginary array that only contained the missing numbers, 
        # then k would directly give us the value of the k-th missing number.
        # However, the real number line also includes valid (non-missing) numbers from the 
        # input array arr, which we must "step over" as we count missing values. During binary search, 
        # left ends up being the count of how many real (non-missing) values we’ve seen before reaching 
        # the k-th missing number. These values are not part of the missing sequence but still count 
        # when moving along the full number line. Therefore, we need to add those left valid numbers 
        # to our target k to get the actual number in the number line: k + left.

        # 1st round:
        # 1, 2, [3], 4, 5, 6, 7, 8, 9, 10, 11
        # 2, 3, [4], 7, 11
        # ---->m ( 1st round m = 2)
        # 4 - 3 = 1. means there are 1 missing number existed here;

        # 2nd round:
        # 1, 2, 3, [4], 5, 6, 7, 8, 9, 10, 11
        # 2, 3, 4, [7], 11
        # ------->m ( 2nd round m = 3)
        # 7 -4 = 3. means there are 3 missing number existed here;

        # 3rd round:
        # 1, 2, 3, 4, [5], 6, 7, 8, 9, 10, 11
        # 2, 3, 4, 7, [11]
        # ---------->m ( 3rd round m = 4)
        # 11 -5 = 6. means there are 6 missing number existed here; containing what we need, which is 5th.
        # 4 (7's correspoding number) + 5th missing= anwser 9

