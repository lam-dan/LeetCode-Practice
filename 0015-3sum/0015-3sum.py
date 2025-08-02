class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array to apply two-pointer approach
        res = []     # This will store the final list of triplets

        # Iterate through each number, considering nums[i] as the first element of the triplet
        for i in range(len(nums)):
            # Skip duplicate numbers for i to avoid duplicate triplets
            if i > 0 and nums[i - 1] == nums[i]:
                continue  # Move to next i if current nums[i] is the same as nums[i - 1]
            # Initialize two pointers
            left = i + 1                # Start left pointer right after i
            right = len(nums) - 1       # Start right pointer at the end of the array

            # Search for two numbers nums[left] and nums[right] such that their sum with nums[i] is 0
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Calculate the sum of the triplet
                if total == 0:
                    # Found a valid triplet, add it to the result
                    res.append([nums[i], nums[left], nums[right]])
                    # Move both pointers inward to look for the next unique pair
                    left += 1
                    right -= 1
                    # Skip duplicate numbers for left pointer to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate numbers for right pointer to avoid duplicate triplets
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:
                    # If total is too big, move the right pointer left to decrease the sum
                    right -= 1
                else:
                    # If total is too small, move the left pointer right to increase the sum
                    left += 1

        return res  # Return the list of all unique triplets that sum to 0