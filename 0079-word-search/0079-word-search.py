class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(i, j, k):
            if k == len(word):
                return True
            # Base Case
            if (
                i < 0 or 
                j < 0 or
                i >= rows or
                j >= cols or # Boundaries of matrix
                board[i][j] != word[k] or  # Not the same word
                (i, j) in path # not in path
            ):
                return False
            path.add((i,j))
            #Check 4 directions, always increment k to update word[k]
            res = (
                dfs(i + 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j - 1, k + 1) 
            )
            #Backtrack
            path.remove((i,j))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0): # k=0 to track index of char in word
                    return True
        return False