class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        count = 0
        minLen = float('inf')
        sIndex = -1
        t_counter = Counter(t)
        window_counter = Counter()
        need = len(t_counter)           # Total unique characters needed to satisfy t

        # Preprocess: filter s to only the necessary characters
        filtered_s = []
        for i in range(len(s)):
            if s[i] in t_counter:
                filtered_s.append((i, s[i]))  # (original index, character)

        for i in range(len(filtered_s)):
            ch = filtered_s[i][1]
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
                window_counter[left_char] -= 1

                if window_counter[left_char] < t_counter[left_char]:
                    count -= 1
                left += 1
        return "" if minLen == float('inf') else s[sIndex:sIndex + minLen]


            



            


        
        

        
            