import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        heap = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if heap and start >= heap[0][0]:
                heapq.heappop(heap)
            heapq.heappush(heap, (end, start))
        return len(heap)

        
