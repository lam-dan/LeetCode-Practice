class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Inuitition is recursion
        # we need to generate all combinations so we use recursion
        # we use backtracking to prune invalid combinations

        target_len = 2 * n
        path = []
        res = []

        def dfs(number_of_open, number_of_closed):
            # Base Case - we reach target length
            if len(path) == target_len:
                res.append("".join(path))
            # Append "(" to path and try adding again but backtrack when path
            # starts to become invalid
            if number_of_open < n:
                path.append("(")
                dfs(number_of_open + 1, number_of_closed)
                path.pop()
            # Append ")" to path and try adding again but backtrack when path
            # start to become invalid
            if number_of_closed < number_of_open:
                path.append(")")
                dfs(number_of_open, number_of_closed + 1)
                path.pop()
        dfs(0,0)
        return res