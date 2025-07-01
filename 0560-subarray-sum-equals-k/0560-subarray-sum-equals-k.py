from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Create hashmap for storing prefix_sum:frequency
        prefix_sums = Counter()
        prefix_sums[0] = 1 # Initialize empty array prefix_sum as frequency 1
        curr_sum = 0 # cumulative sum at current index
        count = 0 # count of subarrays

        for num in nums:
            curr_sum += num
            complement = curr_sum - k # complement of diff between current cumulative sum minus k
            if complement in prefix_sums: #if you've seen complement before
                count += prefix_sums[complement] # increase the count
            prefix_sums[curr_sum] += 1 # increment counter by one for current curr_sum
        return count


