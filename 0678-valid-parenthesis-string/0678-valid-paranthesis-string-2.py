class Solution:
    def checkValidString(self, s: str) -> bool:
        # low  = the minimum possible number of unmatched '(' seen so far
        # high = the maximum possible number of unmatched '(' seen so far
        # We track a *range* of how many opens we could have at any point:
        #   low  → assumes every '*' is used as a ')'
        #   high → assumes every '*' is used as a '('
        # If low ever drops below 0, we reset it to 0 (can't have negative opens).
        # If high ever drops below 0, it means we have too many ')' no matter what, so invalid.
        low = high = 0
        for ch in s:
            if ch == '(': # A '(' always increases both min and max open counts
                low += 1
                high += 1
            elif ch == ')': # A ')' will close one '(' in BOTH best and worst cases
                low -= 1 #   - Best case (low): we had an open to close, so low decreases by 1
                high -= 1 #   - Worst case (high): we must close one, so high decreases by 1
            else:  # ch == '*'
                # '*' is a wildcard — it can be:
                #   1) '(' → increases open count
                #   2) ')' → decreases open count
                #   3) ''  → no change
                low -= 1 # For "low" (best case: try to minimize opens), we treat '*' as ')'
                high += 1 # For "high" (worst case: maximize opens), we treat '*' as '('
            if high < 0: # If high < 0, even in the most optimistic case we have more ')' than '('
                return False # → impossible to balance from here, so return False
            if low < 0: # low should never be negative; negative means we had more closes than opens
                low = 0 # in the best case, which just means we could be perfectly balanced (0)
        return low == 0 # At the end: low == 0 means there is *some* assignment of '*' that results
        # in exactly zero unmatched '(' — i.e., a valid balanced string
