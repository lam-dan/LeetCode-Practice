import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # iterate through values and compare current start time vs previous end time
        if not intervals:
            return 0
        # sort the intervals by start time
        intervals.sort(key = lambda a: a[0]) # Sort by start time
        heap = []

        for start, end in intervals:
            # Compare the current node in the intervals to what was previously pushed into our heap
            if heap and start >= heap[0][0]: # Curr start time compared against Prev end time
                heapq.heappop(heap) # pop the value since we need to free up the room
            # Push into our heap the end times only
            heapq.heappush(heap, (end, start)) # 1) First heap push will be the first intervals
        return len(heap)
            
        

        





