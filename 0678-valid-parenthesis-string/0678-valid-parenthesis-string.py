class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        close_stack = []

        for i in range(len(s)):
            if s[i] == ")":
                close_stack.append(s[i])
            else:
                open_stack.append(s[i])

            if len(close_stack) > len(open_stack):
                return False

        open_stack = []
        close_stack = []

        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                open_stack.append(s[i])
            else:
                close_stack.append(s[i])
            if len(open_stack) > len(close_stack):
                return False
        return True



            