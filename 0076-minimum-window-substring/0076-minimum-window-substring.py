class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        count = 0
        minLen = float('inf')
        sIndex = -1
        t_counter = Counter(t)
        window_counter = Counter()
        need = len(t_counter)           # Total unique characters needed to satisfy t

        for i in range(len(s)):
            window_counter[s[i]] += 1  # Include current character in the window

            # If the current character's count matches the requirement in t, increment count
            if s[i] in t_counter and window_counter[s[i]] == t_counter[s[i]]:
                count += 1

            # When all unique required characters are satisfied, try shrinking the window
            while count == need:
                # Update minimum window if the current window is smaller
                if i - left + 1 < minLen:
                    minLen = i - left + 1
                    sIndex = left
                
                window_counter[s[left]] -= 1 # Shrink the window from the left
                # # If removing this character breaks the requirement, decrement count
                if s[left] in t_counter and window_counter[s[left]] < t_counter[s[left]]:
                    count -= 1
                left += 1
        return "" if minLen == float('inf') else s[sIndex:sIndex + minLen]


            



            


        
        

        
            