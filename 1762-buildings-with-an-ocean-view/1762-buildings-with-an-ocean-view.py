class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = float('-inf')
        answer = []

        for curr in range(len(heights) - 1, -1, -1):
            if heights[curr] > max_height:
                answer.append(curr)
                max_height = heights[curr]
        answer.reverse()
        return answer