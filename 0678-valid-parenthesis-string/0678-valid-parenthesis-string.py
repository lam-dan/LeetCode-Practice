class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Greedy two-pass solution to check if a string with '(', ')', and '*'
        can be interpreted as a valid parentheses sequence.

        Greedy rule: At any point, you cannot have more closing brackets
        than you could possibly match with '(' and '*' seen so far (forward pass),
        and you cannot have more opening brackets than you could possibly match
        with ')' and '*' seen so far (reverse pass).
        """
        # -----------------
        # Pass 1: Left -> Right
        # Ensure we never have "too many" closing parentheses too early.
        # num_open  = count of '(' so far
        # num_close = count of ')' so far
        # num_star  = count of '*' so far (can be '(' or ')' or empty)
        # -----------------
        open_count = 0
        close_count = 0
        star_count = 0

        for i in range(len(s)):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")":
                close_count += 1
            elif s[i] == "*":
                star_count += 1
            
            # If closes exceed all possible opens (including stars-as-opens), fail
            if close_count > open_count + star_count:
                return False

        # -----------------
        # Pass 2: Right -> Left
        # Ensure we never have "too many" opening parentheses too early
        # when scanning from the end.
        # num_open  = count of '(' so far (from the right side)
        # num_close = count of ')' so far (from the right side)
        # num_star  = count of '*' so far (can be ')' or '(' or empty)
        # -----------------

        open_count = 0
        close_count = 0
        star_count = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")":
                close_count += 1
            elif s[i] == "*":
                star_count += 1
            
            # If opens exceed all possible closes (including stars-as-closes), fail
            if open_count > close_count + star_count:
                return False
        
        # Passed both checks -> valid string
        return True
        


        