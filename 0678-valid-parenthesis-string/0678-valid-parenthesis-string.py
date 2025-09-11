class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i in range(len(s)):
            if s[i] == "(":
                left.append(i) # Track positions using index
            elif s[i] == "*":
                star.append(i) # Track positions using index
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        # 2 pointers
        i = len(left) - 1      # top of the 'left' stack
        j = len(star) - 1      # top of the 'star' stack
        while i >= 0 and j >= 0:
            if left[i] > star[j]:
                # latest '(' occurs after latest '*': impossible to match
                return False
            # match them and move both pointers left
            i -= 1
            j -= 1
        # valid iff no '(' remain unmatched
        return i < 0 # No more values in left stack means we have all matches