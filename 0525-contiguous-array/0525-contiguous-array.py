class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Dictionary to store first occurrence of each count value
        # count = difference between number of 1's and 0's seen so far
        # Initialize with count 0 at index -1 to handle subarrays starting at index 0
        count_to_index = {0: -1}

        max_len = 0  # Tracks maximum length of balanced subarray
        count = 0    # Running difference between number of 1's and 0's

        for i, num in enumerate(nums):
            # Treat 1 as +1, 0 as -1
            count += 1 if num == 1 else -1

            # If this count has been seen before, subarray between previous index and current index is balanced
            if count in count_to_index:
                length = i - count_to_index[count]
                max_len = max(max_len, length)
            else:
                # First time seeing this count, store its index
                count_to_index[count] = i

        return max_len  # Return maximum balanced subarray length found