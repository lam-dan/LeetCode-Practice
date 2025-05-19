class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            left = i + 1
            right = len(nums) - 1

            # Sliding window technique
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # if total < target:
                #     result.append([nums[i], nums[left], nums[right]])
                #     left += 1
                #     right -= 1
                #     # Handle duplicate solutions
                #     while left < right and nums[left] == nums[left-1]:
                #         left += 1
                #     while left < right and nums[right] == nums[right+1]:
                #         right -= 1
                # condition when total is > greater than target
                if total > target:
                    right -= 1
                    # while left < right and nums[left] == nums[left-1]:
                    #     left += 1
                    # while left < right and nums[right] == nums[right+1]:
                    #     right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                
        return len(result)
                
                
