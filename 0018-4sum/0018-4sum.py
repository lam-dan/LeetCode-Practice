class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res: List[List[int]] = []

        # Early exit
        if n < 4:
            return res

        for i in range(n - 3):
            # Skip duplicate a's
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optional pruning for the i loop
            min_sum_i = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min_sum_i > target:
                break  # sums will only grow as i increases
            max_sum_i = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
            if max_sum_i < target:
                continue  # even the largest possible with this i is too small

            for j in range(i + 1, n - 2):
                # Skip duplicate b's (with the same i)
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Optional pruning for the j loop
                min_sum_j = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min_sum_j > target:
                    break  # increasing j will only increase sums here
                max_sum_j = nums[i] + nums[j] + nums[n - 1] + nums[n - 2]
                if max_sum_j < target:
                    continue

                # Two pointers for c, d
                left, right = j + 1, n - 1
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
        




            
