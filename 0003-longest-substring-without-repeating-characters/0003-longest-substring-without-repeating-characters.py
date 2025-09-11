from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = right = 0

        res = 0
        for right in range(len(s)):
            if s[right] in chars:
                chars[s[right]] += 1
            else:
                chars[s[right]] = 1
            while chars[s[right]] > 1:
                chars[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res





