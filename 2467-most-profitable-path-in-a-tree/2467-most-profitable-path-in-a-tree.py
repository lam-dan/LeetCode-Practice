class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # Bob simulation
        bob_times = {} #node on root path -> time visited
        
        def dfs(curr, prev, time):
            if curr == 0:
                bob_times[curr] = time
                return True
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if dfs(nei, curr, time + 1):
                    bob_times[curr] = time
                    return True
            return False

        dfs(bob, -1, 0)
        # Alice Simulation - BFS
        queue = deque([(0, 0, -1, amount[0])]) # (node, time, parent, total profit)
        res = float("-inf")

        while queue:
            node, time, parent, profit = queue.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                nei_profit = amount[nei]
                nei_time = time + 1
                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        nei_profit = 0
                    elif nei_time == bob_times[nei]:
                        nei_profit = nei_profit // 2
                queue.append((nei, nei_time, node, profit + nei_profit))
                if len(adj[nei]) == 1:
                    res = max(res, profit + nei_profit)
        return res




