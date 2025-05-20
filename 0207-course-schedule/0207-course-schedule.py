from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        # Create adjacency list
        adj_list = defaultdict(list)
        # Create an ndegree to keep track of all edges for each node
        ndegree = [0] * numCourses
        print(ndegree)


        for u,v in prerequisites:
            adj_list[v].append(u)
            ndegree[u] += 1

        print(adj_list)
        print(ndegree)

        # Create a queue
        queue = deque([])
        print(queue)
        # Add into the queue the nodes that don't have ndegrees
        for node in range(numCourses):
            if ndegree[node] == 0:
                queue.append(node)
        
        print(queue)
        counter = 0

        # Create a global counter

        while queue:
            node = queue.popleft()
            counter += 1

            for nei in adj_list[node]:
                ndegree[nei] -= 1
                if ndegree[nei] == 0:
                    queue.append(nei)
        print(counter)

        return counter == numCourses

        # Iterate through the queue
        # Remove the values from queue
        # Increment the counter
        # Iterate over neighbors
        # For each of the neighbors we're going decrement the degrees
        # now if the neighbor's ndegree is 0, we go ahead and add it to the queue


        # Check if the counter is equal to the number of courses
        # return true
        # else return false
