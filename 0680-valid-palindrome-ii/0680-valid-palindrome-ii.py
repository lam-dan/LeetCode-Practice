class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 2 pointer approach
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(left + 1, right, s) or self.isPalindrome(left, right - 1, s)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

