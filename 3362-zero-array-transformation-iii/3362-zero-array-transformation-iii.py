class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Determines the maximum number of queries that can be removed based on constraints.
        
        Args:
            nums (List[int]): Each index represents a time slot, value = max assignments allowed at that time.
            queries (List[List[int]]): Each query is [arrival_time, deadline_time].
        
        Returns:
            int: The number of queries that can be removed. Returns -1 if constraints can't be satisfied.
        """
        
        # Sort queries by arrival time
        queries.sort(key=lambda x: x[0])

        available = []  # Max-heap for available queries based on deadline (invert sign for max-heap behavior)
        assigned = []   # Min-heap for currently assigned queries based on deadline
        count = 0       # Count of successfully assigned queries
        k = 0           # Pointer to iterate through sorted queries

        # Iterate through each time slot
        for time in range(len(nums)):

            # Remove expired assignments from 'assigned' heap
            while assigned and assigned[0] < time:
                heapq.heappop(assigned)

            # Push available queries that have arrived by current time into the 'available' heap
            while k < len(queries) and queries[k][0] <= time:
                heapq.heappush(available, -queries[k][1])  # Use negative for max-heap
                k += 1

            # Assign as many available queries as allowed by nums[time], ensuring deadlines are valid
            while len(assigned) < nums[time] and available and -available[0] >= time:
                deadline = -heapq.heappop(available)
                heapq.heappush(assigned, deadline)
                count += 1

            # If we couldn't fulfill required assignments for current time, return -1
            if len(assigned) < nums[time]:
                return -1

        # Total queries minus successfully assigned queries gives the number of removable queries
        return len(queries) - count