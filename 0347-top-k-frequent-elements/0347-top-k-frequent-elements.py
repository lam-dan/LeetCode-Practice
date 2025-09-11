from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket_list = [ [] for _ in range(len(nums) + 1)]

        for count, num in count.items():
            bucket_list[num].append(count)

        res = []

        for bucket in reversed(bucket_list):
            for num in bucket:
                res.append(num)
                k -= 1 # Subtract from our total count
                if k == 0:
                    return res
        return -1
                


