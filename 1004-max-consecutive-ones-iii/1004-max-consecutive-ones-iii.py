class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Left boundary of the sliding window
        curr = 0  # Count of zeros flipped to ones within the current window
        ans = 0   # Maximum length of subarray found so far

        # Iterate over the array with the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                # If we encounter a 0, we consider flipping it
                curr += 1
            
            # Shrink the window from the left if the number of flipped zeros exceeds k
            while curr > k:  # WINDOW_CONDITION_BROKEN
                if nums[left] == 0:
                    # If the leftmost number is a zero, we're removing a flip
                    curr -= 1
                # Move the left boundary to the right
                left += 1

            # Update the maximum length of the window
            ans = max(ans, right - left + 1)
        
        return ans


            
