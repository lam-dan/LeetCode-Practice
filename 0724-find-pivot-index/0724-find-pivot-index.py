class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Prefix Sum
        prefix_forwards = [nums[0]]
        prefix_backwards = [nums[-1]]

        for i in range(1, len(nums)):
            prefix_forwards.append(nums[i] + prefix_forwards[-1])
        
        for i in range(len(nums) - 2, -1, -1):
            prefix_backwards.append(nums[i] + prefix_backwards[-1])

        prefix_backwards.reverse()
        print("prefix_fowards", prefix_forwards)
        print("prefix_backwards", prefix_backwards)

        for i in range(len(nums)):
            if prefix_forwards[i] == prefix_backwards[i]:
                return i
        return -1
        




