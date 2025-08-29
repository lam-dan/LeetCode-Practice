class Solution:
    def checkValidString(self, s: str) -> bool:
        # low = smallest number of '(' we might have right now
        # high = largest number of '(' we might have right now
        low = high = 0  

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low = max(0, low - 1)  # ')' reduces '(' count (can't go below 0 for low)
                high -= 1
            else:  # '*'
                # '*' could be ')' -> low-1, '(' -> high+1, or '' -> unchanged
                low = max(0, low - 1)
                high += 1

            # If high goes negative, even the max '(' count can’t match ')' so far → invalid
            if high < 0:
                return False

        # At the end, low==0 means we can choose assignments to make it perfectly balanced
        return low == 0



            