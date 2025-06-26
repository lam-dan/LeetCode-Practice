class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # 2 pointers
        # Sorting 
        # Greedy Approach - making a logically optimal choice at each step
        # You don't backtrack or reconsider previous choices

        # This is so called "binary search on/the answer". How to recognize it?
        # Usually you look at Output: X. And the questions is formed like this: find min out of all max or max of all min.          
        # Also usually it's seen with a greedy algo (like in 2141. Maximum Running Time of N Computers)
        # I prefer to have a separate function that answers a specific question with YES or NO.
        # Similar questions with the same concept:

        # Koko Eating Bananas
        # Capacity To Ship Packages Within D Days
        # Sell Diminishing-Valued Colored Balls
        # Minimum Limit of Balls in a Bag
        # Cutting Ribbons
        # Minimized Maximum of Products Distributed to Any Store
        # Minimum Time to Complete Trips
        # Maximum Candies Allocated to K Children
        # Maximum Tastiness of Candy Basket
        # Minimum Time to Repair Cars

        def count_valid_pairs(max_allowed_diff):
            pairs = 0
            i = 0
            while i + 1 < n:
                if nums[i + 1] - nums[i] <= max_allowed_diff: #Check if the difference of next value vs current is within our threshold of max allowed diff
                    pairs += 1 # increase our pair count
                    i += 1 # increase i to check next value
                i += 1
            return pairs >= p # p is the number of pairs allowed for this problem


        nums.sort()
        n = len(nums)

        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            if count_valid_pairs(mid):
                right = mid
            else:
                left = mid + 1
        return left



        