from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()  # Dictionary to store number → index mappings

        # Iterate through the list with index and value
        for i, num in enumerate(nums):
            complement = target - num  # The value we need to find to form a pair

            # If the complement has been seen before, we found the solution
            if complement in dic:
                # Return the index of the complement and the current index
                return [dic[complement], i]
            else:
                # Otherwise, store the current number and its index
                dic[num] = i

        return []  # Return empty list if no valid pair is found (though problem guarantees one exists)
