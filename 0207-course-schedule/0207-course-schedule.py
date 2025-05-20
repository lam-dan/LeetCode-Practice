from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)        
        ndegree = [0] * numCourses #index is used for tracking nodes 

        for u,v in prerequisites:
            adj[v].append(u)
            ndegree[u] += 1

        # BFS
        q = deque()
        
        for node in range(numCourses):
            if ndegree[node] == 0:
                q.append(node)


        visited = 0 #global counter

        while q:
            node = q.popleft() # node val
            visited += 1

            for nei in adj[node]:
                ndegree[nei] -= 1
                if ndegree[nei] == 0:
                    q.append(nei)

        return numCourses == visited

