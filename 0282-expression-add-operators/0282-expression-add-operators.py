class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        def dfs(i: int = 0, prefix: str = '', value: int = 0, prev: int = 0):
            # Base Case
            if i == len(num) and value == target:
                result.append(prefix)
                return None

            # Try all possible combinations
            for j in range(i + 1, len(num) + 1):
                string = num[i:j] # Take the substring num[i:j]
                number = int(string)
                 # Skip numbers with leading zeros, except for '0' itself
                if len(string) > 1 and num[i] == '0': continue
                if not prefix:
                    dfs(j, string, number, number)
                else:
                    dfs(j, prefix + '+' + string, value + number, number)
                    dfs(j, prefix + '-' + string, value - number, -number)
                    dfs(j, prefix + '*' + string, value - prev + prev * number, prev * number)
        dfs()
        return result


