class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(p1, p2):
            # Base Case
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if p1 >= len(text1) or p2 >= len(text2):
                return 

            if (p1, p2) in memo:
                return memo[(p1, p2)]

            # Recursion
            if text1[p1] == text2[p2]:
                memo[(p1, p2)] = 1 + dfs(p1 + 1, p2 + 1)
                return memo[(p1, p2)]
            else:
                memo[(p1,p2)] = max(dfs(p1, p2+ 1), dfs(p1 + 1, p2))
                return memo[(p1, p2)]

        return dfs(0,0)