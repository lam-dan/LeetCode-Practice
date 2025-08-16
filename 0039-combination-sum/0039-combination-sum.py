class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort()

        def dfs(i, array, prefix_sum):
            if i > len(candidates):
                return
            if prefix_sum == target:
                self.result.append(array.copy())
                return 
            
            for i in range(i, len(candidates)):
                # Base case pruning method
                if prefix_sum + candidates[i] > target:
                    return
                array.append(candidates[i])
                dfs(i, array, prefix_sum + candidates[i])
                array.pop()
        dfs(0, [], 0)
        return self.result
        