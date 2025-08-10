class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array so we can use the two-pointer technique and pruning
        nums.sort()
        res = []  # Final list of unique quadruplets

        # Early exit: need at least 4 numbers for a quadruplet
        if len(nums) < 4:
            return res

        # -------------------------------
        # OUTER LOOP: pick the first number (index i)
        # -------------------------------
        for i in range(len(nums) - 3):  # leave space for j, left, right
            # Skip duplicate values for nums[i] to avoid duplicate quadruplets
            if i == 0 or nums[i] != nums[i - 1]:
                # -------------------------------
                # PRUNE FOR i (smallest and largest possible sums)
                # -------------------------------
                # The smallest possible sum with this i: nums[i] + next 3 smallest numbers
                min_sum_i = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
                if min_sum_i > target:
                    # Since nums is sorted, any later i will only be larger
                    break  # No quadruplet starting from this or future i can reach target

                # The largest possible sum with this i: nums[i] + 3 largest numbers
                max_sum_i = nums[i] + nums[-1] + nums[-2] + nums[-3]
                if max_sum_i < target:
                    # Even the largest possible sum with this i is too small
                    continue  # Try the next i

                # -------------------------------
                # SECOND LOOP: pick the second number (index j)
                # -------------------------------
                for j in range(i + 1, len(nums) - 2):  # leave space for left, right
                    # Skip duplicate values for nums[j] when paired with this nums[i]
                    if j == i + 1 or nums[j] != nums[j - 1]:

                        # -------------------------------
                        # PRUNE FOR j (smallest and largest possible sums)
                        # -------------------------------
                        # The smallest possible sum with this (i, j)
                        min_sum_j = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                        if min_sum_j > target:
                            # Since nums is sorted, increasing j will only increase the sum
                            break  # No further j will work for this i

                        # The largest possible sum with this (i, j)
                        max_sum_j = nums[i] + nums[j] + nums[-1] + nums[-2]
                        if max_sum_j < target:
                            # Even the largest possible sum with this j is too small
                            continue  # Try next j

                        # -------------------------------
                        # TWO-POINTER SEARCH for remaining two numbers (left, right)
                        # -------------------------------
                        left, right = j + 1, len(nums) - 1
                        while left < right:
                            total = nums[i] + nums[j] + nums[left] + nums[right]

                            if total == target:
                                # Found a valid quadruplet
                                res.append([nums[i], nums[j], nums[left], nums[right]])

                                # Move left pointer forward, skipping duplicates
                                left += 1
                                while left < right and nums[left] == nums[left - 1]:
                                    left += 1

                                # Move right pointer backward, skipping duplicates
                                right -= 1
                                while left < right and nums[right] == nums[right + 1]:
                                    right -= 1

                            elif total < target:
                                # Sum too small — move left pointer right to increase sum
                                left += 1
                            else:
                                # Sum too large — move right pointer left to decrease sum
                                right -= 1

        return res
        """
        Time Complexity:
            - Sorting: O(n log n)
            - Outer loop (i): O(n)
            - Second loop (j): O(n)
            - Two-pointer scan: O(n) per (i, j) pair
            - Total worst-case: O(n^3)  (pruning reduces average-case runtime but not worst case)

        Space Complexity:
            - Sorting: O(log n) stack space from Timsort
            - Pointers/variables: O(1) extra space
            - Output list: O(k), where k is the number of quadruplets found
        """




            
