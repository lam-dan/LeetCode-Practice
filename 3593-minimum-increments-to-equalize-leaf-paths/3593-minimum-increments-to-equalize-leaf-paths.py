class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        # Build adjacency list for the undirected tree
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.total_increase = 0  # Track total number of increase operations needed

        def dfs(node, parent):
            """
            Post-order DFS to compute subtree sums and count necessary increase operations.

            Args:
                node: Current node being processed
                parent: The parent node, used to avoid revisiting in undirected graph

            Returns:
                Total sum of the subtree rooted at 'node'
            """
            child_sums = []  # Store sums returned by each child subtree

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue  # Skip the parent to prevent revisiting the same edge
                child_sums.append(dfs(neighbor, node))  # Recursively process child subtrees

            if not child_sums:
                return cost[node]  # Leaf node, subtree sum is simply its own cost

            max_sum = max(child_sums)  # Find the largest subtree sum among children

            # Count how many child subtrees need to be increased to match the largest
            for s in child_sums:
                if max_sum - s > 0:
                    self.total_increase += 1  # Increment count of increase operations
            return max_sum + cost[node]  # Total sum of current subtree includes this node's cost

        dfs(0, -1)  # Start DFS from root node 0, no parent (-1)
        return self.total_increase  # Total operations needed to balance all subtrees
        
        
