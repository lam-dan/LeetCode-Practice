class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # nums = [0,1,3,50,75]
        #         
        # missing = [0,0,2,45,25]

        result = []

        for i in range(len(nums)):

            if nums[i] > lower:
                result.append([lower, nums[i] - 1])
            
            lower = nums[i] + 1

        if lower <= upper:
            result.append([lower, upper])
        
        return result