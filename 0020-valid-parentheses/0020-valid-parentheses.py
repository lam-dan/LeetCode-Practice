class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for i in range(len(s)):
            if s[i] in mapping:
                top_element = stack.pop() if stack else "#"

                if mapping[s[i]] != top_element:
                    return False
            else:
                stack.append(s[i])
        
        if len(stack) > 0:
            return False
        return True