class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Intuition:
        # The core idea is that a palindrome number reads the same forward 
        # and backward — so we only need to compare the first half and the 
        # reversed second half of the number.
        # Negative numbers are not palindrome

        # Numbers endings in 0 can't be palindrome unless the number itself (e.g., 10 != 01)
        if x < 0 or (x % 10 == 0 and x != 0): # e.g. x = -121 or x = 10 → False
            return False

        # Store the original number for comparison later
        original = x # original = 121
        
        # Initialize the reversed_num to build the reversed version of x
        reversed_num = 0 # reversed_num = 0

        # Reverse the digits of x one by one
        while x > 0:
            digit = x % 10 # Extract the last digit digit
            # 1st iteration: digit = 121 % 10 = 1
            # 2nd iteration: digit = 12 % 10 = 2
            # 3rd iteration: digit = 1 % 10 = 1

            reversed_num = reversed_num * 10 + digit # Append the digit to the reversed number
            # 1st iteration: reversed_num = 0 * 10 + 1 = 1
            # 2nd iteration: reversed_num = 1 * 10 + 2 = 12
            # 3rd iteration: reversed_num = 12 * 10 + 1 = 121

            x = x // 10 # Remove the last digit from x
            # 1st iteration: x = 121 // 10 = 12
            # 2nd iteration: x = 12 // 10 = 1
            # 3rd iteration: x = 1 // 10 = 0 → loop exits

        # Compare reversed digit to original
        return reversed_num == original # 121 == 121 → True


