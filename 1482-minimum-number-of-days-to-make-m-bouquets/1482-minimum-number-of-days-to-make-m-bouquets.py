class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Binary Search on patterns, you know the range
        #  Key Takeaways
        # Binary Search on Answer Space is used when:
        # Output is a min/max you can test with YES/NO logic.
        # You can phrase the problem: "Can I achieve X with Y constraints?"
        # Similar problems:
        # Koko Eating Bananas
        # Ship Capacity within D Days
        # Minimum Time to Complete Trips
        # Cutting Ribbons, and others.

        # m = Number of bouquets you must form
        # k = Number of consecutive flowers required to make one bouquet

        # Helper function: Checks if it's possible to make at least m bouquets by 'day_limit'
        def can_make_bouquets(mid):
            total_bouquets = 0      # Total bouquets formed so far
            count_of_flowers = 0       # Current count of consecutive bloomed flowers

            for day in bloomDay:
                if day <= mid:
                    count_of_flowers += 1  # Flower has bloomed by 'day_limit'
                    if count_of_flowers == k:
                        total_bouquets += 1  # One bouquet formed
                        count_of_flowers = 0    # Reset consecutive count
                else:
                    count_of_flowers = 0  # Streak broken, need k consecutive again

            return total_bouquets >= m  # Return True if enough bouquets can be formed

        # Impossible to form m bouquets if not enough flowers
        if m * k > len(bloomDay):
            return -1

        # Binary search boundaries: earliest bloom day to latest bloom day
        left = min(bloomDay)
        right = max(bloomDay)

        # Standard binary search loop to find minimal valid day
        while left <= right:
            mid = (left + right) // 2

            if can_make_bouquets(mid):
                right = mid - 1  # Possible to make bouquets, try earlier days
            else:
                left = mid + 1   # Not enough bouquets, need more days

        # 'left' points to the smallest day where it's possible to form required bouquets
        return left
 

