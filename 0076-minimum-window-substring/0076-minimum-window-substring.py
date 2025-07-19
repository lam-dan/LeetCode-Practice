class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0                    # Left pointer of the sliding window
        count = 0                   # Number of unique characters satisfying the target frequency
        minLen = float('inf')       # Length of the smallest window found so far
        sIndex = -1                 # Start index of the smallest window
        t_counter = Counter(t)      # Frequency of each character in t
        window_counter = Counter()  # Frequency of characters in the current window
        need = len(t_counter)       # Total number of unique characters needed

        # Preprocess: filter s to only the necessary characters
        filtered_s = []
        for i in range(len(s)):
            if s[i] in t_counter:
                filtered_s.append((i, s[i]))  # (original index, character)

        for i in range(len(filtered_s)):
            ch = filtered_s[i][1] # Current character at the right boundary
            window_counter[ch] += 1  # Include current character in the window

            # If the current character's count matches the requirement in t, increment count
            if window_counter[ch] == t_counter[ch]:
                count += 1

            # When all unique required characters are satisfied, try shrinking the window
            while count == need:
                start = filtered_s[left][0] # Original index in s for the current left boundary
                end = filtered_s[i][0] # Original index in s for the current right boundary

                # Update minimum window if the current window is smaller
                if end - start + 1 < minLen:
                    minLen = end - start + 1
                    sIndex = start # Save the start index of the current best window

                # Prepare to shrink the window by removing the character at the left boundary
                left_char = filtered_s[left][1]
                window_counter[filtered_s[left][1]] -= 1

                # If frequency falls below required, decrement count
                if window_counter[left_char] < t_counter[left_char]:
                    count -= 1
                left += 1 # Shrink window from the left
        # Return the smallest window substring or empty string if not found
        return "" if minLen == float('inf') else s[sIndex:sIndex + minLen]


            



            


        
        

        
            