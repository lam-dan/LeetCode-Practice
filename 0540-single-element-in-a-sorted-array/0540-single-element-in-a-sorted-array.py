class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1   # force mid to be even, i.e. the "first of a pair"
            if nums[mid] == nums[mid + 1]:
                left = mid + 2   # pair intact → skip it
            else:
                right = mid      # pair broken → single is at mid or to the left
        return nums[left]


