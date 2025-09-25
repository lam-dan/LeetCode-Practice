class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+', '-', '*', '/'
        }

        for i in range(len(tokens)):
            if tokens[i] in operators:
                if stack and len(stack) >= 2:
                    second = stack.pop()
                    first = stack.pop()
                    if tokens[i] == "+":
                        stack.append(first + second)
                    elif tokens[i] == "-":
                        stack.append(first - second)
                    elif tokens[i] == "*":
                        stack.append(first * second)
                    elif tokens[i] == "/":
                        stack.append(int(first / second))
            else:
                stack.append(int(tokens[i]))

        return stack[-1]
