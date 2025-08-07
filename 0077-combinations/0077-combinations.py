class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.results = []

        def dfs(array, first_num):
            # Base Case
            if len(array) == k:
                self.results.append(array.copy())
                return

            last_num = n - (k - len(array)) + 1
            
            for i in range(first_num, last_num + 1):
                array.append(i)
                dfs(array, i + 1)
                array.pop()
        dfs([], 1)
        return self.results