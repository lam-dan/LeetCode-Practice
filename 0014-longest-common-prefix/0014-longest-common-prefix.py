    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # ["flower","flow","flight"]
        first_word = strs[0]

        for i in range(len(first_word)): # Loop over each character index i in the first string "flower"
            char = strs[0][i] # char = "f"
            print("char", char)
            # iterate through of the list
            for j in range(1, len(strs)):
                word = strs[j]
                print("word", word)
                # If we're over the boundaries of this word OR there's a mismatch
                if i >= len(word) or word[i] != char:
                    # Mistmatch is found, return the common prefix up to but not including index `i`
                    return first_word[:i]
        # If we finish the loop without returning, all characters in strs[0] matched in all strings
        return first_word
