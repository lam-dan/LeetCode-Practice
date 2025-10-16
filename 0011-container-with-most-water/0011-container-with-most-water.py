class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## 2 pointer approach
        # opposite ends
        # while loop + if/else statement 
        # ++left ++right
        left = 0
        right = len(height) - 1
        max_area = float(-inf)
        min_height = float(inf)

        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area