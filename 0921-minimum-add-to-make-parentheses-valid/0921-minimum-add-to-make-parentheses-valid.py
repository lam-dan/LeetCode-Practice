
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if len(stack) > 0 and stack[-1] == "(" and s[i] == ")":
                stack.pop()
                continue
            stack.append(s[i])
        return len(stack)

        # Time Complexity: O(N)
        # Space Coplexity: O(1)