class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [100,4,200,1,3,2]
        # 100 - once we find the starting value, 
        # we try to increase the length as much as we can
        # 200
        # 1 -> 2 -> 3 -> 4 maxn of length

        # 100
        # 1 -> 2 -> 3 -> 4
        # 200
        unique = set(nums)
        print(unique)
        # n = len(nums)

        # print(n)
        longest = 0

        for num in nums:
            # print(i)
            if (num - 1) not in unique:
                length = 0
                while (num + length) in unique:
                    length += 1
                longest = max(longest, length)
        return longest

