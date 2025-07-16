class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        left = 0
        right = 0
        # Traverse both lists until one is exhausted
        # Intuition Behind Why It Works
        # Both firstList and secondList are sorted by start times.

        # At every step, you compare one interval from each list:
        # firstList[left] and secondList[right].

        # To check if these two intervals overlap, you:

        # start = max(firstList[left][0], secondList[right][0])
        # end = min(firstList[left][1], secondList[right][1])
        # The intersection starts at the later of the two start points.
        # The intersection ends at the earlier of the two end points.

        # If start <= end, there is a valid overlap, so you add it to the result.
        while left < len(firstList) and right < len(secondList):

            start = max(firstList[left][0], secondList[right][0])
            end = min(firstList[left][1], secondList[right][1])

            if start <= end:
                res.append([start, end])
            
            if firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                right += 1

        return res
        