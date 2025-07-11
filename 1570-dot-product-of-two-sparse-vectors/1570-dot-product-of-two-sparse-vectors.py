class SparseVector:
    def __init__(self, nums: List[int]):
        # Store only non-zero engtries as (index, value) pairs
        self.arr = [(idx, num) for idx,num in enumerate(nums) if num != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        curr_arr = self.arr
        vec_arr = vec.arr

        ans = 0
        for idx, val in curr_arr:
            # Binary search based on index since indexes are sorted by default
            matched_val = self.binary_search(vec_arr, idx)
            if matched_val != float('inf'):
                ans += val * matched_val
        return ans

    def binary_search(self, arr, target_idx):
        # Handle vector arrs which is all sparse: [0,0,0,0]
        if not arr:
            return float('inf')

        left, right = 0, len(arr) -1
        # Finding Index Target is not gauranteed
        # Thus, we use while left + 1 < right
        # Post-processing will follow after where fall backs are needed
        # if we can't find what we're looking for
        while left + 1 < right:
            mid = (left + right) // 2
            mid_idx, mid_val = arr[mid]

            if mid_idx == target_idx:
                return mid_val
            elif mid_idx > target_idx:
                right = mid
            else:
                left = mid
        # Post processing if target_idx is not found:
        # Check if left and right pointers are in boundaries
        # Check if left and right indexes are equal to target infex
        if left < len(arr) and arr[left][0] == target_idx:
            target_val = arr[left][1]
            return target_val
        if right < len(arr) and arr[right][0] == target_idx:
            target_val = arr[right][1]
            return target_val

        return float('inf')
        # Time Complexity is O(n) where n is all entires in the input list
        # Space Complexity is O(k) where k is the number of non-zero entries
        # in that vector
            





        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)