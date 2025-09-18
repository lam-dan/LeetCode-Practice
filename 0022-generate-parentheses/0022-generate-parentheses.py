class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []                  # to store all valid combinations
        target_len = 2 * n        # each valid sequence has length 2n
        path = []                 # current sequence being built (as a list of chars)
        def dfs(number_of_opens: int, number_of_closed: int) -> None:
            # Base case: if we’ve built a full-length sequence, add to result
            if len(path) == target_len:
                res.append("".join(path))
                return  # stop exploring further
            # Option 1: add an open parenthesis "("
            # Allowed if we still have unused opens left
            if number_of_opens < n:
                path.append("(")                           # choose
                dfs(number_of_opens + 1, number_of_closed) # explore
                path.pop()                                 # undo (backtrack)
            # Option 2: add a close parenthesis ")"
            # Allowed only if more opens have been used than closes
            if number_of_closed < number_of_opens:
                path.append(")")                           # choose
                dfs(number_of_opens, number_of_closed + 1) # explore
                path.pop()                                 # undo (backtrack)
        # Start DFS with no opens or closes placed
        dfs(0, 0)
        return res
        # -----------------------------------------------
        # Time Complexity:
        #   - There are C_n valid sequences (n-th Catalan number).
        #   - Each sequence has length 2n, and building it costs O(n).
        #   - Total: O(C_n * n).
        #
        # Space Complexity:
        #   - Recursion stack depth = O(2n) = O(n).
        #   - Path buffer = O(n).
        #   - Result storage = O(C_n * n) (size of the output itself).
        #   - Auxiliary space (ignoring output): O(n).
        # -----------------------------------------------