class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert to set for O(1) lookups and to avoid duplicate words
        words = set(wordDict)
        # Memoization cache:
        #   key   = position in string (start index of remaining substring)
        #   value = True/False whether s[pos:] can be segmented
        memo = {}
        def dfs(pos: int) -> bool:
            """
            Returns True if substring s[pos:] can be segmented
            into one or more words from 'words', else False.
            """
            # Base case: if we've consumed all characters,
            # it means the whole string was successfully segmented
            if pos == len(s):
                return True
            # Return cached result if already computed
            if pos in memo:
                return memo[pos]
            # Try every word in the dictionary
            for word in words:
                # Check if 'word' matches the substring starting at pos
                if s.startswith(word, pos):
                    # If it matches, recursively check the remainder
                    next_pos = pos + len(word)
                    if dfs(next_pos):
                        memo[pos] = True  # Cache result
                        return True       # Found a valid segmentation
            # No valid segmentation found from this position
            memo[pos] = False
            return False
        # Start DFS from the beginning of the string
        return dfs(0)
