class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0 # Total count of palindromic substrings

        for i in range(len(s)):
            # Count odd-length palindromes centered at s[i]
            total += self.center_expand(s, i, i)
            # Count even-length palindromes centered between s[i] and s[i+1]
            total += self.center_expand(s, i, i + 1)
        return total        

    def center_expand(self, s, left, right):
        count = 0

        # Expand outward as long as the character match and we're in bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1 # Found a palindrome
            left -= 1 # Expand leftward
            right += 1 # Expand rightward
        return count
