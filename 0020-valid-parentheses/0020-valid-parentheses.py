class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
            }
        stack = []
        for i in range(len(s)):
            if s[i] in mapping:

                if len(stack) > 0:
                    top_element = stack.pop()
                else:
                    top_element = None
                
                if top_element != mapping[s[i]]:
                    return False
            else:
                stack.append(s[i])
        if len(stack) > 0:
            return False
        return True


