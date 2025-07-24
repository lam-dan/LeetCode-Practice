class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # Dictionary to group strings by shifting pattern

        for word in strings:
            key = []  # List to hold relative character shifts
            
            # Example: for s = "abc", ord('a') = 97
            # word[0] = 'a'
            # 'a' → (97 - 97) % 26 = 0
            # 'b' → (98 - 97) % 26 = 1
            # 'c' → (99 - 97) % 26 = 2
            # Key = (0, 1, 2)
            for char in word:
                shift = (ord(char) - ord(word[0])) % 26  # Shifting each character of the word to the first character of the word
                # We use modulo 26 to handle wrap-around in the alphabet.
                # For example: "az" → 'z' - 'a' = 25 → (25) % 26 = 25
                # But "ba" → 'a' - 'b' = -1 → (-1 % 26) = 25 (in Python, negative % yields positive equivalent)
                # So both "az" and "ba" get the same pattern: [0, 25]
                # This allows the grouping to be **cyclically invariant**.
                key.append(shift)
            # Group strings with the same key (i.e., same shifting pattern)
            result[tuple(key)].append(word)
        # Example input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
        # Groups would be:
        # ["abc", "bcd", "xyz"]      → key = (0,1,2)
        # ["az", "ba"]               → key = (0,25)
        # ["acef"]                   → key = (0,2,4,5)
        # ["a", "z"]                 → key = (0,)
        return list(result.values())  # Return grouped string lists

