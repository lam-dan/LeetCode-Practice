class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Start from the rightmost digits (least significant digits), just like in manual addition
        i, j = len(num1) - 1, len(num2) - 1

        carry = 0  # Holds overflow from one digit sum to the next, like carrying over in pen-and-paper math
        result = []  # We'll build the result here, in reverse order

        # Loop until we've processed both strings completely AND used up any carry
        while i >= 0 or j >= 0 or carry:
            # Get digit from num1 or 0 if i is out of range
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            # Get digit from num2 or 0 if j is out of range
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            # Add the two digits and the carry from the previous step
            total = digit1 + digit2 + carry

            # Intuition: This is like adding digits column-by-column from right to left
            # For example:   456
            #              +  77
            #            --------
            #               533
            # Step 1: 6+7=13 → write down 3, carry 1
            # Step 2: 5+7+1=13 → write down 3, carry 1
            # Step 3: 4+0+1=5 → write down 5

            # Append the last digit of the total to the result (what you'd write down in the current column)
            result.append(str(total % 10))

            # Update the carry to be used in the next iteration (leftward column)
            carry = total // 10  # This is equivalent to carrying the "tens" place over

            # Move one digit to the left in both numbers
            i -= 1
            j -= 1

        # We built the number in reverse order (from least significant to most), so reverse it
        return ''.join(reversed(result))

        # Time Complexity is O(max(n,m))
        # where n and m are the length of each string, whichever is bigger
        # each iteration we are processing one digit at a time from both strings until they both run out.

        # Space Complexity is O(max(n,m))
        # The result stores one character for each digit of the sum

