class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2 pointers
        # i to keep track of position of iteration
        # j to updates in the array
        i = 1
        j = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j # Return the index of our last update

        # Time Complexity is O(n) - worst case we iterate through n number of numbers
        # Space Complexity is O(1) - pointers only

        

            


        