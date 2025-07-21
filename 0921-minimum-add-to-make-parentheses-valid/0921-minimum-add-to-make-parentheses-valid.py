
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_bracket_count = 0
        min_count = 0

        for i in range(len(s)):

            if s[i] == "(":
                open_bracket_count += 1
            elif s[i] == ")":
                if open_bracket_count > 0:
                    open_bracket_count -= 1
                else:
                    min_count += 1

            
        return open_bracket_count + min_count
        
        
    


            




        # Time Complexity: O(N)
        # Space Coplexity: O(N)