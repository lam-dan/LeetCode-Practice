class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        N = len(num)

        def dfs(i: int = 0, value: int = 0, prev: int = 0, expr: list = []):
            """
            i: Current index in num
            value: Evaluated total so far
            prev: Last operand (for multiplication precedence)
            expr: List of characters building the expression
            """
            if i == N:
                if value == target:
                    result.append(''.join(expr))
                return

            for j in range(i + 1, N + 1):
                part = num[i:j]
                number = int(part)

                # Skip numbers with leading zeros
                if len(part) > 1 and part[0] == '0':
                    continue

                if i == 0:
                    # First operand, no operator
                    expr.extend(part)
                    dfs(j, number, number, expr)
                    del expr[-len(part):]
                else:
                    # Addition
                    expr.append('+')
                    expr.extend(part)
                    dfs(j, value + number, number, expr)
                    del expr[-(len(part) + 1):]

                    # Subtraction
                    expr.append('-')
                    expr.extend(part)
                    dfs(j, value - number, -number, expr)
                    del expr[-(len(part) + 1):]

                    # Multiplication
                    expr.append('*')
                    expr.extend(part)
                    dfs(j, value - prev + prev * number, prev * number, expr)
                    del expr[-(len(part) + 1):]

        dfs()
        return result


