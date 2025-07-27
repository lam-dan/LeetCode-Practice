class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Intuition:
        # The core idea is that a palindrome number reads the same forward 
        # and backward — so we only need to compare the first half and the 
        # reversed second half of the number.
        # Number: 1221
        # First half: 12
        # Second half reversed: 12 → Match

        # Number: 12321
        # First half: 12
        # Second half reversed: 123 → Drop the middle digit (3) → 12 → Match

        # Negative numbers are not palindrome
        # Numbers endings in 0 can't be palindrome unless the number itself (e.g., 10 != 01)
        if x < 0 or (x % 10 == 0 and x != 0): # e.g. x = -121 or x = 10 → False
            return False

        # Store the original number for comparison later
        original = x  # original = 121 (odd) or 1221 (even)

        # Initialize the reversed_num to build the reversed version of x
        reversed_num = 0  # reversed_num = 0

        # Reverse the digits of x one by one
        while x > 0:
            digit = x % 10  # Extract the last digit

            # Odd example (x = 121):
            # 1st iteration: digit = 121 % 10 = 1
            # 2nd iteration: digit = 12 % 10 = 2
            # 3rd iteration: digit = 1 % 10 = 1

            # Even example (x = 1221):
            # 1st iteration: digit = 1221 % 10 = 1
            # 2nd iteration: digit = 122 % 10 = 2
            # 3rd iteration: digit = 12 % 10 = 2
            # 4th iteration: digit = 1 % 10 = 1

            reversed_num = reversed_num * 10 + digit  # Append digit to the reversed number

            # Odd (121):
            # 1st: reversed_num = 0 * 10 + 1 = 1
            # 2nd: reversed_num = 1 * 10 + 2 = 12
            # 3rd: reversed_num = 12 * 10 + 1 = 121

            # Even (1221):
            # 1st: reversed_num = 0 * 10 + 1 = 1
            # 2nd: reversed_num = 1 * 10 + 2 = 12
            # 3rd: reversed_num = 12 * 10 + 2 = 122
            # 4th: reversed_num = 122 * 10 + 1 = 1221

            x = x // 10  # Remove the last digit from x

            # Odd (121):
            # 1st: x = 121 // 10 = 12
            # 2nd: x = 12 // 10 = 1
            # 3rd: x = 1 // 10 = 0

            # Even (1221):
            # 1st: x = 1221 // 10 = 122
            # 2nd: x = 122 // 10 = 12
            # 3rd: x = 12 // 10 = 1
            # 4th: x = 1 // 10 = 0

        return reversed_num == original  
        # Odd: 121 == 121 → True
        # Even: 1221 == 1221 → True


