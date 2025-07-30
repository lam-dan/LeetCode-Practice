class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Removes all adjacent k-duplicate characters from the string `s`.

        A stack-based approach is used where each entry is a (character, count)
        tuple representing the current streak of repeated characters.

        When the count reaches `k`, that group is removed by not re-adding it to the stack.

        Example:
        Input:  s = "deeedbbcccbdaa", k = 3
        Output: "aa"
        Explanation: 
          - Remove "eee" → "ddbbcccbdaa"
          - Remove "ccc" → "ddbbdaa"
          - Final output: "aa"

        Time Complexity: O(n)
        - Each character is pushed and popped from the stack at most once.

        Space Complexity: O(n)
        - In the worst case (no removals), the stack stores one entry per character.
        """
        stack = [] # Stack to track (character, count) tuples
        # Traverse input string character by character
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                # Same as previous character
                prev_char, prev_count = stack.pop()
                new_count = prev_count + 1

                if new_count == k:
                    continue # Reached k duplicates, so we skip pushing, this removes the entire group
                if new_count < k:
                    stack.append((s[i], new_count)) # push back into stack since it's not at k yet
            else:
                stack.append((s[i], 1)) # pushing current char into stack with count of 1
        
        return ''.join(char * count for (char, count) in stack) # Rebuild string from tuple containing char and count

        # Time Complexity is O(n) where n is the number of characters in the string s
        # Space Complexity is O(n) where n is the number of characters in the string s

                

                