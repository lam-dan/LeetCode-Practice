class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat_bananas(bananas_per_hours):
            total_hours = 0
            for banana in piles:
                total_hours += math.ceil(banana/bananas_per_hours)
            return total_hours <= h

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            if can_eat_bananas(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left