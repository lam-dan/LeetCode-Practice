class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # https://youtu.be/Q2Tw6gcVEwc?t=116
        if numRows == 1 or numRows >= len(s):
            return s
        result = []
        step = 2 * (numRows - 1) # one full zigzag section
        # step represents the number of characters you pass through to get to the same row position
        for r in range(numRows): # 0, 1, 2
            i = r # i = 0, !1, 2
                                        #0 1 2 3 !4 5 6 7 8 9 10 11 12 13
            while i < len(s): #  n = len(!P !A Y !P !A L I S !H I R   I  !N G)
                result.append(s[i])
                # if middle rows also have a diagonal hit inside the same section
                if 0 < r < numRows - 1:
                    # 1 + (4 - 2 * 1)
                    # 1 + 2 = 3
                    j = i + (step - 2 * r) # find the index of the diagonal based on the step
                    # 3 < 
                    if j < len(s): #if we're still in the boundaries of the string
                        result.append(s[j])
                i += step # jump to next section (same row) 0, 4
                # [P A H N A P]
        return "".join(result)

        # O(n)
        # O(1)




