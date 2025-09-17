class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        hottest = 0  # Track the hottest temperature seen so far (moving backwards)

        # Traverse from the last day to the first
        for i in range(n - 1, -1, -1):
            # If today's temp is >= anything in the future, no warmer day exists
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue

            # Otherwise, there *is* a warmer day ahead
            j = i + 1
            # Jump ahead until we find a warmer temperature
            # Analogy to "Jump Game":
            #   - In Jump Game, nums[i] tells you how far you can skip.
            #   - Here, ans[j] tells you how many days to skip forward.
            while temperatures[j] <= temperatures[i]:
                j += ans[j]  # use precomputed answers to skip ahead efficiently

            # The distance to the next warmer day is how far we jumped
            ans[i] = j - i

        return ans