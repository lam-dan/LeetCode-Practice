class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)  # Sort jobs descending for better pruning
        self.res = sum(jobs)     # Worst-case upper bound (all jobs to one worker)
        worker = [0] * k         # Track total workload per worker

        def dfs(i):
            if i == len(jobs):
                self.res = min(self.res, max(worker))
                return
            
            seen = set()
            for j in range(k):
                if worker[j] in seen:
                    continue  # Skip duplicate worker states
                seen.add(worker[j])

                worker[j] += jobs[i]
                
                if max(worker) < self.res:  # Prune if worse than current best
                    dfs(i + 1)
                
                worker[j] -= jobs[i]

                if worker[j] == 0:
                    break  # Optimization: only try first empty worker slot

        dfs(0)
        return self.res