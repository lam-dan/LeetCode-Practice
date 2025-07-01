class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Two Sum (Hash Map) + Prefix Sums
        count = 0
        total = 0

        hash_map = defaultdict(int)
        hash_map[0] = 1

        # prefixSum = [nums[0]]
        for i in range(0, len(nums)):
            total += nums[i]
            # prefixSum.append(prefixSum[-1] + nums[i])
            count += hash_map[total - k]
            hash_map[total] += 1
        return count

        

        

        print(prefixSum)