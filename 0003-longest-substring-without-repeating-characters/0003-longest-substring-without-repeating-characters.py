class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        # 2 windows
        # No Duplicates
        # Length calculation
        uniques = set()
        length = 0
        left = 0

        for i in range(len(s)):
            while s[i] in uniques:
                uniques.remove(s[left])
                left += 1
            uniques.add(s[i])
            length = max(length, len(uniques))
        return length
