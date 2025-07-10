class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1) We want to find a breakout point at n, because at n + 1 - all the 
        # numbers will be greater than arr[n] > arr[n + 1]. For example, arr = [2,1,5,4,3,0,0], 
        # the break point here is the arr[n] = 1 and arr[n + 1] = 5. You can draw it out in a graph
        # to visually see where the dip in the graph is.

        # 2) At this point in time, we have to decide whether to take the 1 or anything to the 
        # right of n, in this case next greater would not be 5, we only want slightly increasing, 
        # so it's 3 => 5, 4, 3. So to find someone greater than one, but the smallest number 
        # that's greater than 1. In this case, it's 3. Now we swap the 3 with 1, so we have:
        # [2,1,5,4,3,0,0]
        # [2,3,5,4,1,0,0]
        # So now we have [2,1] > [2,3], what about the remaining numbers?

        # 3) Now the remaining numbers don't matter, we try to keep it small so we can slowly 
        # increase it in the next permutation.Therefore, in this step we will sort the remaining 
        # numbers to [2,3,0,0,1,4,5]

        # Potential Edge Cases:
        # [5,4,3,2,1]
        # If there is no dip in the graph, then idx = -1, becuase you just reverse the array
        # and that will be your lexographically smallest value.
        # if idx == -1: arr = reverse(arr)

        # Identify index for breakpoint
        # idx = -1
        # for i in range(len(nums) - 2, -1, -1):
        #     if nums[i] < nums[i + 1]: # Find the Dip in the graph
        #         idx = i
        #         break

        # if idx == -1:
        #     return nums.reverse()

        # # print(idx)
        # # Swapping process
        # for i in range(len(nums) - 1, idx + 1, - 1):
        #     if nums[i] > nums[idx]: # If the current number is greater than the index, swap them
        #         tmp = nums[i]
        #         nums[i] = nums[idx]
        #         nums[idx] = tmp
        #         break

        # # print(nums)
        
        # # The replacement must be in place and use only constant extra memory. - Per requirements
        # nums[idx:] = reversed(nums[idx:]) # modifies


        # # print(nums)
        # return nums


        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        j = len(nums) - 1
        while j >= i and nums[j] <= nums[i-1]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]

        nums[i:] = reversed(nums[i:])

        

            

