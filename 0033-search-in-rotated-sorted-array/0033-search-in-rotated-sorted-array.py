class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search in rotated sorted array
        left = 0
        right = len(nums) - 1 

        while left <= right:
            mid = (left + right) // 2
            print("left", left)
            print("right", right)
            print("mid", mid)
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]: # Search is left rotated sorted array
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            


