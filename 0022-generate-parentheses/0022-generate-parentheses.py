class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        OPEN = "("
        CLOSE = ")"
        target_len = 2 * n
        path = []

        def dfs(number_of_opens, number_of_closed):
            # If our current path is equal to the target len
            if len(path) == target_len:
                res.append("".join(path))

            # Add "(" if we still have some left to place
            if number_of_opens < n:
                path.append("(")
                dfs(number_of_opens + 1, number_of_closed)
                path.pop()

            # Add ")" if we still have some left to close
            if number_of_closed < number_of_opens:
                path.append(")")
                dfs(number_of_opens, number_of_closed + 1)
                path.pop()
        dfs(0,0)
        return res