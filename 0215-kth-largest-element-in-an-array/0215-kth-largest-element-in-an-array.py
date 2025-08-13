from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Find min and max values
        max_num, min_num = max(nums), min(nums)
        bucket_range = max_num - min_num

        # Create buckets as lists
        bucket = [[] for _ in range(bucket_range + 1)]

        # Place numbers in buckets (directly storing values)
        # We take place the num but we subtract by min to offset negative values
        for num in nums:
            bucket[num - min_num].append(num)
        print(bucket)

        flat = [value for i in bucket for value in i]
        i = len(flat) - k

        print(flat)

        # Flatten the bucket array in reverse order and extract kth largest
        # flattened = [num for i in range(len(bucket) - 1, -1, -1) for num in bucket[i]]
        # print(flattened)
        return flat[i]
