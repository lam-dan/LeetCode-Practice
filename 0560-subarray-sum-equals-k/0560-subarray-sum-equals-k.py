class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        prefix_sum[0] = 1
        count = 0
        curr_sum = 0


        for i in range(len(nums)):
            curr_sum += nums[i]
            complement = curr_sum - k

            if complement in prefix_sum:
                count += prefix_sum[complement]

            if curr_sum in prefix_sum:
                prefix_sum[curr_sum] += 1
            else:
                prefix_sum[curr_sum] = 1
        return count
            

            