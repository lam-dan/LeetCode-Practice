class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucketList = [[] for _ in range(len(nums) + 1)]
        print("COUNT", count)
        print("BUCKETLIST", bucketList)

        for num, freq in count.items():
            bucketList[freq].append(num)

        print("BUCKETLIST 2", bucketList)

        res = []
        for freq in range(len(bucketList) - 1, -1, -1):
            for num in bucketList[freq]:
                res.append(num)
                if len(res) == k:
                    return res