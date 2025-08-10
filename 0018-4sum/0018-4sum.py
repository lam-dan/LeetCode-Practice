class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        # Early exit
        if len(nums) < 4:
            return res

        for i in range(len(nums) - 3):
            # Skip duplicate a's
            if i == 0 or nums[i] != nums[i - 1]:
                # Prune for i
                min_sum_i = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
                if min_sum_i > target:
                    break
                max_sum_i = nums[i] + nums[i - 1] + nums[i - 2] + nums[i - 3]
                if max_sum_i < target:
                    continue

                for j in range(i + 1, len(nums) - 2):
                    # Skip duplicate b's (with the same i)
                    if j == i + 1 or nums[j] != nums[j - 1]:
                    # Two pointers for c, d
                        left = j + 1
                        right = len(nums) - 1
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
        




            
