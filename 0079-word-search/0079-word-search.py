class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])


        def dfs(i, j, c):
            if len(word) == c:
                return True
            if(
                i < 0 or 
                j < 0 or
                i >= rows or
                j >= cols or
                board[i][j] != word[c] or
                board[i][j] == "#"
            ):
                return False

            board[i][j] = "#"

            res = (
                dfs(i + 1,j, c + 1) or
                dfs(i - 1,j, c + 1) or
                dfs(i,j + 1, c + 1) or
                dfs(i,j - 1, c + 1)
            )
            board[i][j] = word[c]
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False