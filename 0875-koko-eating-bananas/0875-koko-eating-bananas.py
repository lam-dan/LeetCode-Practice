class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function: Checks if it's possible to eat all bananas within h hours at a given speed
        def can_eat_bananas(bananas_per_hour):  # also called "speed"
            total_hours = 0  # Total time needed at this eating speed
            for banana in piles:
                # At speed = bananas_per_hour, Koko takes ceil(pile_size / speed) hours for each pile
                # Example: pile=7, speed=3 → ceil(7/3)=3 hours
                total_hours += math.ceil(banana / bananas_per_hour)
            # Return True if the total hours is within the allowed limit
            return total_hours <= h  # Can she finish within h hours?

        # Search space is [1 .. max(piles)] bananas per hour
        # 1 = slowest (1 banana/hour), max(piles) = fastest needed (clear biggest pile in 1 hour)
        left = 1
        right = max(piles)

        # Binary search over possible speeds
        while left <= right:
            mid = (left + right) // 2  # Trial eating speed (bananas/hour)

            if can_eat_bananas(mid):
                # If she can finish at this speed, maybe she can go slower
                # so shrink the search space to [left .. mid-1]
                right = mid - 1
            else:
                # If she cannot finish, speed is too slow → need faster
                # so search in [mid+1 .. right]
                left = mid + 1

        # When the loop ends:
        # - left points to the smallest speed that still allows her to finish
        # - right points to the last "too fast" candidate
        return left  # minimal valid eating speed

