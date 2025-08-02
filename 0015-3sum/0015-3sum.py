class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # if nums[i] > 0:
            #     break
            
            if i == 0 or nums[i - 1] != nums[i]:
                # Two Pointer
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                    elif total > 0:
                        right -= 1
                    else:  
                        left += 1
        return res