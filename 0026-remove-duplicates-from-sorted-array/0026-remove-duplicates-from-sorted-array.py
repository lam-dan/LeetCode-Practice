class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_index = 1

        for i in range(1, len(nums)):
            # If previous value is not equal to current value
            if nums[i - 1] != nums[i]:
                # Updating the insert index in our main array
                nums[insert_index] = nums[i]
                # Incrementing insert index count by 1
                insert_index += 1
        return insert_index

        # Time Complexity is O(n) where n is the number of integers in nums
        # Space Complexity is O(1) since we don't create any data structures

