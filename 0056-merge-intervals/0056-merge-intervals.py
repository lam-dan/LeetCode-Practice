class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
               merged[-1] = [merged[-1][0], max(intervals[i][1], merged[-1][1])]
            else:
                merged.append(intervals[i])
            
        return merged


