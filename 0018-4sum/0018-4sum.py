class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        # Early exit
        if n < 4:
            return res

        for i in range(n - 3):
            # Skip duplicate a's
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, n - 2):
                    # Skip duplicate b's (with the same i)
                    if j == i + 1 or nums[j] != nums[j - 1]:
                    # Two pointers for c, d
                        left = j + 1
                        right = n - 1
                        while left < right:
                            total = nums[i] + nums[j] + nums[left] + nums[right]
                            if total == target:
                                res.append([nums[i], nums[j], nums[left], nums[right]])
                                # Move left/right past duplicates
                                left += 1
                                while left < right and nums[left] == nums[left - 1]:
                                    left += 1
                                right -= 1
                                while left < right and nums[right] == nums[right + 1]:
                                    right -= 1
                            elif total < target:
                                left += 1
                            else:
                                right -= 1
        return res
        




            
