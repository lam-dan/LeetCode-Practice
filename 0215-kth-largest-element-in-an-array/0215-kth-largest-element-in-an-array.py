class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = k - 1  # kth largest -> index in a descending-partitioned array

        def partition3(lo, hi):
            """
            3-way partition (descending):
            After partition:
              nums[lo:lt]       > pivot
              nums[lt:gt+1]    == pivot
              nums[gt+1:hi+1]   < pivot
            Returns (lt, gt): the inclusive range where elements equal pivot ended up.
            """
            p = random.randint(lo, hi)
            pivot = nums[p]
            nums[p], nums[hi] = nums[hi], nums[p]  # move pivot to end temporarily

            # Dutch National Flag pointers
            lt = lo         # next position to place an element > pivot
            i = lo          # current scan index
            gt = hi         # next position to place an element < pivot

            while i <= gt:
                if nums[i] > pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] < pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            return lt, gt

        lo, hi = 0, len(nums) - 1
        while True:
            lt, gt = partition3(lo, hi)

            if lt <= target <= gt:
                # target falls inside the == pivot block; any element there is the answer
                return nums[lt]
            elif target < lt:
                hi = lt - 1
            else:
                lo = gt + 1