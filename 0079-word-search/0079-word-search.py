class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(i,j,k):
            if k == len(word):
                return True
            # Base Cases
            if ( 
                i < 0 or
                j < 0 or
                i >= rows or
                j >= cols or
                board[i][j] != word[k] or
                (i, j) in path
            ):
                return False
            #Adding it to the path
            path.add((i,j))

            #Recursive Calls
            # All directions up, down, left, right
            res = (
                dfs(i + 1, j, k + 1) or 
                dfs(i, j + 1, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j - 1, k + 1)
            )
            # Remove the path from our path
            # Backtracking
            path.remove((i,j))

            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False