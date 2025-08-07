class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Classic BackTracking Problem
        # 1. We need to explore all valid combinations
        # You're tasked with finding all combinations of k numbers from [1, n]. 
        # That means we need to systematically explore all possible choices of numbers, but:
        # Not allow duplicates (e.g. [1, 2] and [2, 1] are the same → pick numbers in increasing order)
        # Not go beyond size k
        # Explore one choice, and then back up to try the next one
        # This is exactly what backtracking is built for:

        # 2. Backtracking builds a combinatorial tree
        # Each level of recursion represents picking the next number:
        # At level 0: pick any number from 1 to n-k+1
        # At level 1: pick from the next available numbers
        # Until we hit size k, then we backtrack and try another path
        # This tree of decisions is a natural fit for recursion + backtracking.

        # 3. Backtracking = Efficient + Clean
        # You avoid unnecessary work by pruning early (don’t explore paths longer than k)
        # You don't need to generate all subsets and then filter — you only build valid ones
        # You get compact code that handles all branching cases
        self.results = []

        def dfs(array, first_num):
            # Base Case
            if len(array) == k:
                self.results.append(array.copy())
                return
            for num in range(first_num, n + 1):
                array.append(num)
                dfs(array, num + 1)
                array.pop()

        dfs([], 1)
        return self.results


