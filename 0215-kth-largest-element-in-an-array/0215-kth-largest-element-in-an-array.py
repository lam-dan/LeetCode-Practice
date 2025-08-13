class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert k (1-indexed kth largest) into the "target index" if array were sorted in descending order
        # Example: kth largest = 1 → index 0; kth largest = 2 → index 1, etc.
        target = k - 1  

        def partition3(lo, hi):
            """
            Partition nums[lo:hi+1] into 3 sections using the Dutch National Flag algorithm (in descending order):
                nums[lo:lt]     > pivot
                nums[lt:gt+1]  == pivot
                nums[gt+1:hi+1] < pivot
            Returns:
                lt, gt (start and end indices of the == pivot block)
            This lets us skip over the whole block of equals in one step, avoiding O(n^2) on duplicates.
            """
            # Randomly choose a pivot index to minimize chance of worst-case
            p = random.randint(lo, hi)
            pivot = nums[p]

            # Swap pivot with the last element temporarily
            nums[p], nums[hi] = nums[hi], nums[p]

            # Initialize Dutch National Flag pointers
            lt = lo    # Boundary for elements > pivot
            i = lo     # Current index being scanned
            gt = hi    # Boundary for elements < pivot

            while i <= gt:
                if nums[i] > pivot:
                    # Current element is greater → swap it into left partition
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] < pivot:
                    # Current element is smaller → swap it into right partition
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                    # Note: i not incremented here because swapped element from nums[gt] hasn't been checked yet
                else:
                    # Current element equals pivot → leave in place, just move forward
                    i += 1

            # Return the start and end indices of the pivot-equal block
            return lt, gt

        lo, hi = 0, len(nums) - 1  # Search boundaries for Quickselect

        while True:
            # Partition current subarray and get equal block boundaries
            lt, gt = partition3(lo, hi)

            if lt <= target <= gt:
                # Target index is inside the == pivot block → return pivot value
                return nums[lt]
            elif target < lt:
                # Target index is in the "greater than pivot" partition → search left side
                hi = lt - 1
            else:
                # Target index is in the "less than pivot" partition → search right side
                lo = gt + 1