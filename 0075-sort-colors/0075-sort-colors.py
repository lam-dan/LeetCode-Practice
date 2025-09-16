class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0

        high = len(nums) - 1
        # 2 pointer approach
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                # tmp = nums[mid]
                # nums[mid] = nums[low]
                # nums[low] = tmp
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                # tmp = nums[high] 
                # nums[high] = nums[mid]
                # nums[mid] = tmp
                high -= 1
        return nums
    


        