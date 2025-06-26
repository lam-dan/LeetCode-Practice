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
                    if count_of_flowers == k: # Found k consecutive bloomed flowers → Form 1 bouquet
                        total_bouquets += 1  # One bouquet formed
                        count_of_flowers = 0    # Reset streak for next bouquet
                else:
                    # Flower hasn't bloomed yet → Streak broken, reset consecutive count
                    count_of_flowers = 0
            return total_bouquets >= m  # Return True if enough bouquets can be formed

        # Impossible to form m bouquets if not enough flowers
        if m * k > len(bloomDay):
            return -1

        # Doesn't require sorting for binary search
        # Binary Search on Answer Space:
        # You search for the minimum or maximum feasible value
        # You define a logical range, independent of array ordering
        # Here, array order doesn't affect when flowers bloom relative to a given day_limit
        # The only thing that matters:
        # For a mid day, which flowers have bloomed (day <= mid)
        # Count consecutive valid flowers
        # Order can stay as provided

        # Binary search boundaries:
        # Minimum possible day is when the first flower blooms (min of bloomDay)
        # Maximum possible day is when the last flower blooms (max of bloomDay)
        left = min(bloomDay)
        right = max(bloomDay)

        # Standard binary search loop to find minimal valid day
        while left <= right:
            mid = (left + right) // 2

            if can_make_bouquets(mid):
                # Possible to make bouquets by 'mid' day → Try earlier days to minimize
                right = mid - 1
            else:
                # Not enough bouquets by 'mid' day → Need more days
                left = mid + 1
        # After loop, 'left' points to the smallest valid day where enough bouquets can be formed
        return left
 

