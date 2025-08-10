class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        # At each point in time we have the running total of the left sum 
        # we check to see if that left sum is equal to the right side by the formula
        # total sum of the nums array subtracted by the left sum and the current value of the pointer
        # this will give us the sum on the right hand side.
        for i in range(len(nums)):
            if left_sum == (total_sum - left_sum - nums[i]):
                return i
            left_sum += nums[i] # If they're not equal, continue adding current value to perfix sum
        return -1

        # Time Complexity is O(n)
        # Space Complexity is O(1)

        
