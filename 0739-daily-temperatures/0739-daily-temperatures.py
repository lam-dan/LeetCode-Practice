class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        ans = [0] * n
        hottest = 0  # Track the hottest temperature seen so far (moving backwards)

        # Traverse from the last day to the first
        for i in range(n - 1, -1, -1):
            # If today's temp is >= anything in the future, no warmer day exists
            if temps[i] >= hottest:
                hottest = temps[i]
                continue

            # Otherwise, there *is* a warmer day ahead
            j = i + 1
            # Jump ahead until we find a strictly warmer temperature.
            #
            # IMPORTANT: we must use <= here, not <.
            # Why? Because "warmer" means strictly greater.
            # If we used <, the loop would stop at equal temperatures,
            # which are NOT warmer, and we'd give wrong answers.
            #
            # Counterexample 1: temps = [73, 73, 74]
            #   Expected: [2, 1, 0]
            #   Using < would stop at day 1 (73 == 73) → incorrectly [1, 1, 0].
            #
            # Counterexample 2: temps = [71, 72, 72, 73]
            #   Expected: [1, 2, 1, 0]
            #   Using < would stop day 1 at day 2 (72 == 72) → incorrectly [1, 1, 1, 0].
            #
            while temps[j] <= temps[i]:
                j += ans[j]  # skip forward using precomputed answers

            # The distance to the next warmer day is how far we jumped
            ans[i] = j - i

        return ans