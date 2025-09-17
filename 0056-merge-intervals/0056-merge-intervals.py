class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key = lambda x : x[0])
        result = [intervals[0]]

        for i in range(len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1] = [ result[-1][0], max(result[-1][1], intervals[i][1])]
            else:
                result.append(intervals[i])
        return result
