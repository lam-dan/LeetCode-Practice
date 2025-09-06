class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s

        out = []
        step = 2 * (numRows - 1)


        print("step", step)
        
        for r in range(numRows):
            i = r
            while i < n:
                out.append(s[i])

                if 0 < r < numRows - 1:
                    j = i + (step - 2*r)
                    if j < n:
                        out.append(s[j])
                
                i += step
        return "".join(out)




