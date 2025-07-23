class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # Dictionary to group strings by shifting pattern

        for s in strings:
            key = []  # List to hold relative character shifts
            
            # Example: for s = "abc", ord('a') = 97
            # 'a' → (97 - 97) % 26 = 0
            # 'b' → (98 - 97) % 26 = 1
            # 'c' → (99 - 97) % 26 = 2
            # Key = (0, 1, 2)

            for c in s:
                shift = (ord(c) - ord(s[0])) % 26  # Normalize each character relative to first
                key.append(shift)

            # Group strings with the same key (i.e., same shifting pattern)
            result[tuple(key)].append(s)

        # Example input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
        # Groups would be:
        # ["abc", "bcd", "xyz"]      → key = (0,1,2)
        # ["az", "ba"]               → key = (0,25)
        # ["acef"]                   → key = (0,2,4,5)
        # ["a", "z"]                 → key = (0,)
        
        return list(result.values())  # Return grouped string lists

