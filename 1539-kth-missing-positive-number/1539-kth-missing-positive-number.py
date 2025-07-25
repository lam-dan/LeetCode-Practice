class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Can't apply binary search since target is missing
        # Can't apply binary search on answers - only applicable on min or max
        # Not the case
        # Need to figure out where the answer fits between the the numbers in the arr
        # Figure out the 2 nearby indexes
        # Figure out the missing numbers at each index by taking current value and subtracting
        # from previous value
        #  0 1 2 3 4
        # [2,3,4,7,11]
        # [1,1,1,3,6]
        left = 0 
        right = len(arr) - 1

        while left <= right:

            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return left + k



