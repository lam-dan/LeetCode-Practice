class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(nums)
        if N % size:
            return False
        freq = Counter(nums)
        nums.sort()
        for num in nums:
            if freq[num]:
                for cur in range(num, num + size):
                    freq[cur] -= 1
                    if freq[cur] < 0:
                        return False
        return True