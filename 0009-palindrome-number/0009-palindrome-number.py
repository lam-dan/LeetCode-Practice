class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Checks whether an integer is a palindrome without converting it to a string.
        This efficient version reverses only half the digits and compares.
        
        Time Complexity: O(log₁₀(n)) — processes half of the digits
        Space Complexity: O(1) — uses constant extra space
        """

        # Step 1: Handle special cases
        # Negative numbers are never palindromes (e.g., -121)
        # Numbers ending in 0 (e.g., 10, 100) can't be palindromes unless the number is 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Step 2: Prepare two halves
        # left_half will shrink from the front
        # reversed_right_half will build the reversed back half
        left_half = x
        reversed_right_half = 0

        # Step 3: Build reversed_right_half until it catches up with or surpasses left_half
        while left_half > reversed_right_half:
            last_digit = left_half % 10                     # Get the last digit of the front half
            reversed_right_half = reversed_right_half * 10 + last_digit  # Append to the reversed back half
            left_half //= 10                                # Remove last digit from left_half

            # === Example: Even-length x = 1221 ===
            # Iteration 1: last_digit = 1
            #   left_half = 122, reversed_right_half = 1
            # Iteration 2: last_digit = 2
            #   left_half = 12, reversed_right_half = 12 → stop

            # === Example: Odd-length x = 12321 ===
            # Iteration 1: last_digit = 1
            #   left_half = 1232, reversed_right_half = 1
            # Iteration 2: last_digit = 2
            #   left_half = 123, reversed_right_half = 12
            # Iteration 3: last_digit = 3
            #   left_half = 12, reversed_right_half = 123 → stop

        # Step 4: Compare halves
        # Even number of digits: left_half == reversed_right_half
        # Odd number of digits: middle digit in reversed_right_half doesn't matter → remove it using // 10
        return (
            left_half == reversed_right_half or
            left_half == reversed_right_half // 10
        )