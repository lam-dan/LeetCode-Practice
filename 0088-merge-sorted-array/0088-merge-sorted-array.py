class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Merge two sorted arrays nums1 and nums2 into nums1 in-place.
        nums1 has enough trailing space (length m + n) to hold elements from both arrays.
        
        Time Complexity: O(m + n)  — each element is considered at most once
        Space Complexity: O(1)     — in-place, uses only constant extra space
        """
        # p1: index of last valid element in nums1 (before the extra space)
        p1 = m - 1
        # p2: index of last element in nums2
        p2 = n - 1
        # p3: index of the last position in nums1 (full size m+n)
        p3 = m + n - 1
        # Only need to keep looping until we've placed all of nums2's elements.
        # If nums2 is exhausted, nums1's remaining prefix is already sorted.
        while p2 >= 0:
            # If nums1 still has elements left (p1 >= 0) AND the current nums1 element
            # is larger than the current nums2 element, take from nums1.
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]  # Place larger element at the end
                p1 -= 1                # Move pointer in nums1
            else:
                # Otherwise, take from nums2 (either it's larger, or nums1 is exhausted)
                nums1[p3] = nums2[p2]
                p2 -= 1                # Move pointer in nums2
            
            # Move the placement pointer (p3) one step left after placing an element
            p3 -= 1

        # Time Complexity is O(n + m)
        # Space Complexity is O(1)
