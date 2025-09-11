from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [ [] for _ in range(len(nums) + 1)]

        for count, num in count.items():
            bucket[num].append(count)

        res = []
        for i in range(len(bucket) -1, -1, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                k -= 1 # Subtract from our total count
                if k == 0:
                    return res
        return -1
                


