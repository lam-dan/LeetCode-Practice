class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if an integer is a palindrome without converting to a string.
        This optimized solution only reverses half the number.

        Time Complexity: O(log₁₀(n)) — Processes half the digits.
        Space Complexity: O(1) — Uses constant extra space.
        """
        # Step 1: Handle special edge cases
        # Negative numbers are not palindromes due to '-' sign
        # Numbers ending in 0 (e.g., 10, 100) can't be palindromes unless x == 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Step 2: Initialize the reversed second half
        reversed_half = 0

        # Step 3: Reverse digits until x <= reversed_half
        # This loop will stop once we've reversed half of the digits
        while x > reversed_half:
            digit = x % 10                           # Get the last digit
            reversed_half = reversed_half * 10 + digit  # Append to reversed_half
            x = x // 10                                  # Drop the last digit from x
            # Example: x = 1221 (even length)
            # Iteration 1: digit = 1, reversed_half = 1, x = 122
            # Iteration 2: digit = 2, reversed_half = 12, x = 12 → stop loop

            # Example: x = 12321 (odd length)
            # Iteration 1: digit = 1, reversed_half = 1, x = 1232
            # Iteration 2: digit = 2, reversed_half = 12, x = 123
            # Iteration 3: digit = 3, reversed_half = 123, x = 12 → stop loop

        # Step 4: Compare front half and reversed back half
        # Case 1: Even number of digits → x == reversed_half
        # Case 2: Odd number of digits → x == reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10