class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0 # Running prefix sum modulo k
        mod_seen = {0: -1} # Map of mod result -> earliest index seen

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k # Update cumulative sum mod k

            if prefix_mod in mod_seen:
                # Check fo subarrayb length at least 2
                if i - mod_seen[prefix_mod] > 1:
                    return True # Found valid subarray
            else:
                mod_seen[prefix_mod] = i # Store first occurence of this mod value
        return False #No valid subarray