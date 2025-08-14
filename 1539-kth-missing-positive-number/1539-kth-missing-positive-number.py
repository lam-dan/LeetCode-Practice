class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return k + left

        # Time Complexity is O(n)
        # Space Complexity is O(1)
