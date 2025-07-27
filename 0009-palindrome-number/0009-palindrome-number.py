class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Checks whether an integer is a palindrome by reversing only the second half.
        Uses a numeric equivalent of the two-pointer technique.

        Time Complexity:
            - O(log₁₀(x)) if x is the numeric value because the number of times you can 
            divide x by 10 until it reaches 0 is ≈ log₁₀(x)
            
            More intuitive:
            - O(n) if n is the number of digits in x (we process roughly n/2 digits)

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
        # Step 3: Simulate the two-pointer traversal
        # Instead of comparing digits at the ends, we reconstruct the right half in reverse
        while left_half > reversed_right_half:
            # Step 1) Build Right Side Going from Right to Left
            # We build right side first because it starts as 0
            last_digit = left_half % 10 # Remove last digit from original number x                    
            reversed_right_half = reversed_right_half * 10 + last_digit  # Build the reversed right side

            # Step 2) Build Left Side Going from Left to Right
            # Move "left pointer" to the right
            # We build left half later after since it starts with the original number 
            left_half = left_half // 10 # Remove last digit from original number x

            # Two-pointer analogy: we move inward from both sides
            # left_half: digits from the front → shrinking
            # reversed_right_half: digits from the back → reversed and growing

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

        # Step 4: Compare two "halves" of the number
        # Even-length: left_half == reversed_right_half
        # Odd-length:  left_half == reversed_right_half // 10 (drop middle digit)

        # Example: x = 12321
        # Final: left_half = 12, reversed_right_half = 123
        # reversed_right_half // 10 = 12 → match
        return (
            left_half == reversed_right_half or
            left_half == reversed_right_half // 10
        )

    