class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows > len(s) - 1:
            return s

        result = []
        # number of steps to get to next character in the 2D matrix
        steps = 2 * (numRows - 1)

        for r in range(numRows): # 0, 1, 2
            i = r

            while i < len(s): 
                result.append(s[i])

                if 0 < r < numRows - 1: # Within the boundaries of the middle index of the matrix
                    j = i + (steps - 2 * r)
                    if j < len(s):
                        result.append(s[j])
                i += steps
        return "".join(result)