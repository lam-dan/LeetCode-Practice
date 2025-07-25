class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Negative numbers are not palindromes.
        #         Also, numbers ending with 0 are not palindromes unless the number is 0 itself.
        # Example: -121 -> False, 10 -> False (because it becomes 01 when reversed)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Step 2: Initialize a variable to store the reversed second half of the number.
        reversed_half = 0

        # Step 3: Reverse the last half of the digits from x.
        # We stop when x <= reversed_half, meaning we've processed at least half of the digits.
        while x > reversed_half:
            digit = x % 10              # Take the last digit of x
            reversed_half = reversed_half * 10 + digit  # Add it to the reversed_half
            x //= 10                    # Remove the last digit from x

            # Example Walkthrough: x = 1221
            # Iteration 1: digit = 1, reversed_half = 1, x = 122
            # Iteration 2: digit = 2, reversed_half = 12, x = 12 → stop (x == reversed_half)

        # Step 4: Check if the number is a palindrome.
        # Case 1 (even digits): x == reversed_half
        #   Example: 1221 → x=12, reversed_half=12 → True
        # Case 2 (odd digits): x == reversed_half // 10 (we remove the middle digit)
        #   Example: 12321 → x=12, reversed_half=123 → 123//10 = 12 → x == reversed_half//10 → True

        return x == reversed_half or x == reversed_half // 10