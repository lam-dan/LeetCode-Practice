class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort(key = lambda x: x[0])

        for i in range(len(intervals)):
            if stack and stack[-1][1] >= intervals[i][0]:
                stack[-1] = [stack[-1][0], max(intervals[i][1], stack[-1][1])]
            else:
                stack.append(intervals[i])
        return stack