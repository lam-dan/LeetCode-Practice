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
            # We only update pointers if we found a new longer one
            if max_len > right - left + 1: 
                half = max_len // 2 # Calculate half the length so we can adjust outward from center i
                # If the palindrome is even-length like ("abba"), we shift the left pointer forward by 1
                # This is because the center is between i and i+1, not exactly on i
                if max_len % 2 == 0:
                    left = i - half + 1 # Update global left pointer (start of palindrome)
                    right = i + half # Update global right pointer (end of palindrome)
                # For odd-length palindromes (e.g., racecar), center is exactly at i
                else:
                    left = i - half # Update global left pointer (start of palindrome)
                    right = i + half # Update global right pointer (end of palindrome)

        return s[left:right + 1] # Return the longest palindrome substring 

        # ---------------------------------------------------------------------
        # Time Complexity: O(n^2)
        #   - We iterate over each character in the string (O(n))
        #   - For each character, we expand around it (and between it and the next one)
        #   - In the worst case (e.g., "aaaa..."), each expansion could scan the entire string (O(n))
        #   - So total: O(n) * O(n) = O(n^2)
        #
        # Space Complexity: O(1)
        #   - We only use a few integer variables for tracking indices and lengths
        #   - No dynamic programming table, recursion, or additional data structures
        # ---------------------------------------------------------------------
                