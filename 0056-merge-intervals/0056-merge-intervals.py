class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])

        merged = [intervals[0]] # to keep track of all non overlapping intervals that was the results of merging
        for i in range(len(intervals)):
            
            if intervals[i][0] <= merged[-1][1]: # Condition to merge
                merged[-1] = [merged[-1][0], max(merged[-1][1], intervals[i][1])]
            else:
                merged.append(intervals[i])

        return merged
        
