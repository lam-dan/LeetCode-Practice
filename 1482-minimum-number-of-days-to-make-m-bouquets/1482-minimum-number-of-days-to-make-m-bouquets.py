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

        def get_num_of_bouquets(mid):
            num_of_bouquets = 0
            num_of_flowers = 0

            for day in bloomDay:
                if day <= mid:
                    num_of_flowers += 1
                    if num_of_flowers == k:
                        num_of_bouquets += 1
                        num_of_flowers = 0
                else:
                    num_of_flowers = 0

            return num_of_bouquets >= m

        if m * k > len(bloomDay):
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)

        while left <= right:
            mid = (left + right) // 2

            if get_num_of_bouquets(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
 

