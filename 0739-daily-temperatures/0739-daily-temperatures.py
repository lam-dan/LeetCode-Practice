class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotic Decreasing Stack, as we add indices in the stack, the stack
        # is sorted in a descending order
        n = len(temperatures)
        ans = [0] * n
        stack = []  # stack stores indices of days that are still "unresolved"
                    # i.e., we haven't yet found a warmer temperature for them
        # Traverse from left to right
        for i, temp in enumerate(temperatures):
            # While the stack is not empty AND today's temperature is warmer
            # than the temperature at the index on top of the stack...
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                # We found the next warmer day for day j
                ans[j] = i - j   # distance between days
                # Example: if temps[j] = 71 and temps[i] = 72, then ans[j] = i-j
            # Push the current index onto the stack because we don't yet know
            # when (or if) a warmer day will come for today.
            stack.append(i)
        return ans