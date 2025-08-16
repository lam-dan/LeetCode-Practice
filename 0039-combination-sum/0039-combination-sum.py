class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # DFS 
        # index = 0
        # backtrack
        # Remove the value after our dfs call 
        # Base case is going to be whenever we have >8
        # return from the case - pop the last value from the array
        # we want to copy the arry once we hit our target
        # Iterate through all indexes 
        self.result = []
        def dfs(i, total):
            # Base Case
            if i >= len(candidates) or sum(total) > target:
                return 
            if sum(total) == target:
                self.result.append(total.copy())
                return

            total.append(candidates[i])
            dfs(i, total)
            total.pop()
            dfs(i + 1, total)
        dfs(0, [])

        return self.result
