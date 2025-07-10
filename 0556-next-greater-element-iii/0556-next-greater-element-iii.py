class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))

        idx = -1

        # Reverse the list and find pivot
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i + 1]: #If the current number is greater than the index, swap them
                idx = i
                break
        
        print("nums 1", nums)

        # Handle Edge Case where there is no pivot in the graph
        if idx == -1:
            return -1
        
        # Swap stopping at the idx
        for i in range(len(nums) - 1, idx, -1):
            if nums[i] > nums[idx]:
                tmp = nums[i]
                nums[i] = nums[idx]
                nums[idx] = tmp
                break
        
        # Reverse remainder of the list to the right of the breakpoint idx
        nums[idx + 1:] = list(reversed(nums[idx + 1:]))

        # print("nums 2", nums)
        result = int("".join(nums)) 
        return result if result <= 2**31 - 1 else -1

        