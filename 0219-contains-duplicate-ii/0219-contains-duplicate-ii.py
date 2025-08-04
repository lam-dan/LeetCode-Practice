
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initialize an empty set to represent the sliding window of the last k elements
        window = set()

        # Iterate through each element in nums with index i
        for i in range(len(nums)):
            # If nums[i] is already in the window, we've found a duplicate within k distance
            if nums[i] in window:
                return True  # Duplicate found within k distance

            # Add the current element to the window
            window.add(nums[i])

            # Maintain the window size to be at most k
            # If the window has grown larger than k, remove the oldest element (nums[i - k])
            # This simulates sliding the window forward by one step
            if len(window) > k:
                window.remove(nums[i - k])

        # If no duplicates are found within k distance, return False
        return False
