class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Pattern
        # 2 pointers 
        # Break Down into 3 parts
        n = len(intervals)
        res = []
        i = 0
        # Left Section
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # Middle Section - Merge
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        # Last Remaining Arrays
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
