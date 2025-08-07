class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Knutt Morris KMP Algorithm for O(n) time complexity where n is the number of 
        # elements in haystack
        # However, the trade off is O(m) space where m is the longer array of haystack or needle   
        # Edge case: empty needle should return 0
        if not needle:
            return 0

        # Step 1: Build the LPS (Longest Prefix Suffix) table
        # Example:
        #   needle = "ababaca"
        #   lps    = [0, 0, 1, 2, 3, 0, 1]
        # Explanation:
        #   - lps[i] tells us the length of the longest prefix which is also a suffix
        #     for the substring needle[0:i+1]
        #   - At index 4 ('a'): prefix="aba", suffix="aba" → lps[4] = 3
        #   - At index 5 ('c'): no match, so lps[5] = 0
        #   - At index 6 ('a'): prefix="a", suffix="a" → lps[6] = 1
        # This LPS table allows the search to skip redundant comparisons after mismatches.
        lps = self.build_lps(needle)

        # Step 2: Search needle in haystack using the LPS table
        # For example:
        #   haystack = "abababacababcababaca"
        #   needle   = "ababaca"
        #   match should be found starting at index 13
        i = 0  # pointer for haystack
        j = 0  # pointer for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                # Characters match: move both pointers forward
                i += 1
                j += 1

                if j == len(needle):
                    # If j has reached the end of needle, full match is found
                    # haystack[i - j : i] == needle
                    return i - j  # return start index of match
            else:
                if j > 0:
                    # Mismatch after some matches
                    # Instead of restarting from j = 0, use the LPS table to resume matching
                    # We know that needle[0..j-1] matched, so we fallback to the length of the
                    # longest proper prefix which is also a suffix, given by lps[j - 1]
                    # Example: if j = 4 and mismatch occurs, fallback to j = lps[3] = 2
                    j = lps[j - 1]
                else:
                    # No match yet, just move to the next character in haystack
                    i += 1

        # No match found
        return -1

    def build_lps(self, pattern: str) -> list:
        """
        Build the Longest Prefix Suffix (LPS) array.
        lps[i] = length of the longest proper prefix which is also a suffix
        in pattern[0:i+1]
        """
        lps = [0] * len(pattern)  # Initialize LPS array
        length = 0  # Length of the previous longest prefix suffix
        i = 1       # Start from the second character

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                # Match: extend the current prefix-suffix
                length += 1
                lps[i] = length
                i += 1
            else:
                if length > 0:
                    # Mismatch: fallback to shorter prefix using previous LPS value
                    length = lps[length - 1]
                else:
                    # No prefix match at all, set LPS[i] to 0
                    lps[i] = 0
                    i += 1
        return lps
