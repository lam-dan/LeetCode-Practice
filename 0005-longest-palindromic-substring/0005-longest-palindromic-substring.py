class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Two-pointer expansion technique from the center
        def center_expand(left, right):
            # Expand outward within bounds and characters match 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 # Expand left pointer from center
                right += 1 # Expand right pointer from center
            # Return the length of the palindrome (overshot by 1 on both sides)
            return right - left - 1

        left = 0
        right = 0

        for i in range(len(s)):
            len1 = center_expand(i,i) # Try expanding around a single character (odd-length palindrome)
            len2 = center_expand(i, i + 1) # Try expanding around two characters (even-length palindrome)

            max_len = max(len1, len2) # Take longer of the two expansions
            # If this palindrome is longer than the previous one
            if max_len > right - left + 1: 
                half = max_len // 2 # Half the length of the palindrome to calculate
                # For even length palindrome ("abba")
                if max_len % 2 == 0:
                    left = i - half + 1 # Update left pointer (start of palindrome)
                    right = i + half # Update right pointer (end of palindrome)
                # For odd-length palindrome (e.g., racecar)
                else:
                    left = i - half # Update left pointer (start of palindrome)
                    right = i + half # Update right pointer (end of palindrome)
                    
        return s[left:right + 1] # Return the longest palindrome substring 
                