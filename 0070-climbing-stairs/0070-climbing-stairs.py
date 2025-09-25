class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)

        def dfs(i: int, n: int, memo: List[int]) -> int:
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] > 0:
                return memo[i]
            memo[i] = dfs(i + 1, n, memo) + dfs(
                i + 2, n, memo
            )
            return memo[i]

        return dfs(0, n, memo)

