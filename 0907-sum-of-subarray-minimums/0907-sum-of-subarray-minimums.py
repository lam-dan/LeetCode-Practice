class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Combinations - is the number of selections
        # Example: Choosing A, B, C → ABC, BAC, CBA are the same combination.
        # Selecting 3 people from a group of 10 to form a team. The
        # number of combinations from a team of 10.

        # Permutations - is the number of unique order of elements
        # Example: Arranging A, B, C → ABC and CAB are different permutations.

        # In this case, it would be the number of contiguous combinations.
        # Sliding Window/ 2 Pointers - Dynamic Size, but can't think of fail condition to move left pointer
        # DFS/BFS based on index - however, it must be unique indexes on each call stack frame, BFS only queue index + 1 indexes
        # DP? Pick/Not Pick Algorithm
        # Monotonic Stack - left to right - Time Complexity is O(n^2) since it requires a nested for loop
        MOD = 10 ** 9 + 7
        stack = []   # Monotonic increasing stack to store indices
        total = 0    # Sum of minimums for all subarrays

        # Iterate through the array + 1 extra iteration to flush the stack
        for i in range(len(arr) + 1):
            
            # Current element is arr[i] if within bounds; otherwise 0 to trigger final stack processing
            curr = arr[i] if i < len(arr) else 0

            # Maintain monotonic increasing stack

            # Is the previous element in the monotic stack greater than or equal to the current element
            while stack and arr[stack[-1]] >= curr:
                
                mid = stack.pop()  # Index of the element to process as minimum
                left = stack[-1] if stack else -1  # Index to the left boundary (exclusive)
                right = i  # Current index serves as the right boundary (exclusive)

                # Number of subarrays where arr[mid] is the minimum:
                # - (mid - left) choices for left boundary
                # - (right - mid) choices for right boundary
                count = (mid - left) * (right - mid)

                # Contribution of arr[mid] as minimum in those subarrays
                total += arr[mid] * count
                

            # Push current index onto the stack
            stack.append(i)

        # Return total sum modulo 1e9+7 as required
        return total % MOD



