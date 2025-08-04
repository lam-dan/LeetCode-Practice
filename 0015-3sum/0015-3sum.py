class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # 2 pointers
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue

            if i == 0 or nums[i] != nums[i -1]:
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    
                    if total == 0:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total > 0:
                        right -= 1
                    else: 
                        left += 1
        return result


            