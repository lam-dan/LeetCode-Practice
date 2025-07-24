from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()

        for i, num in enumerate(nums):
            complement = target - num
            if complement not in dic:
                dic[num] = i
            else:
                return [dic[complement], i]
        return []
