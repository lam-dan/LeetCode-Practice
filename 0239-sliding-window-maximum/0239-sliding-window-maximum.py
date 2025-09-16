from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        monotonic_stack = deque() # to store indices of our window
        # maximum values at the front
        # minimum values at the end of the deque
        result = []

        for r in range(len(nums)):
            # Boundary check to remove elements that are outside of our
            # sliding window
            if monotonic_stack and monotonic_stack[0] < r - k + 1:
                monotonic_stack.popleft()

            # Remove elements that are smaller than current
            # shrink our queue based on the current values that are smaller
            while monotonic_stack and nums[monotonic_stack[-1]] <= nums[r]:
                monotonic_stack.pop()

            # Append 
            monotonic_stack.append(r)

            # Check if we're within window size and append to the result
            if r >= k - 1:
                result.append(nums[monotonic_stack[0]])
        return result



