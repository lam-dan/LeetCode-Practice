class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        # Backtracking algorithm
        def dfs(r, c, i):
            # Base Case
            if len(word) == i:
                return True
            # Falsy Check - Out of bounds, or visited
            if (
                r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] == 0 or board[r][c] != word[i]
            ):
                return False
            # Mark as visited
            board[r][c] = 0
            
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            # Back track if after searching in remaing directions and the next character
            # of the word doesn't exist
            board[r][c] = word[i]
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False