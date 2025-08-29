class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []

        # Pass 1: Scan from Left to Right
        for i in range(len(s)):
            if s[i] == "(":
                open_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            elif s[i] == ")":
                # Removal process from stacks
                if len(open_stack) > 0:
                    open_stack.pop()
                elif len(star_stack) > 0:
                    star_stack.pop()
                else:
                    return False
            else:
                return False

        # # Pass 2: Scan from Right to Left
        while len(open_stack) > 0 and len(star_stack) > 0:
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False
        return len(open_stack) == 0
        


        