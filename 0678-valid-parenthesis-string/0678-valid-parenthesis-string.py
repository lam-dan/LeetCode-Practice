class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []

        for i in range(len(s)):
            if s[i] == "(":
                open_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            elif s[i] == ")":
                if len(open_stack) == 0 and len(star_stack) == 0:
                    return False
                    
                if len(open_stack) > 0:
                    open_stack.pop()
                elif len(star_stack) > 0:
                    star_stack.pop()

        while len(open_stack) > 0 and len(star_stack) > 0:
            if open_stack.pop() > star_stack.pop():
                return False

        if len(open_stack) > 0:
            return False
        return True
        


        